// reading a text file
#include <iostream>
#include <fstream>
#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;
// todo: get input via GET request using e.g. https://github.com/jpbarrette/curlpp

// https://stackoverflow.com/a/46931770
std::vector<std::string> split(const std::string& s, const std::string& delimiter) {
  size_t pos_start = 0, pos_end, delim_len = delimiter.length();
  std::vector<std::string> res;

  while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
    std::string token = s.substr(pos_start, pos_end - pos_start);
    pos_start = pos_end + delim_len;
    res.push_back(token);
  }

  res.push_back(s.substr(pos_start));
  return res;
}

int main() {
  string line;
  fstream my_file ("inputs/day1.txt");

  std::vector<int> ids_a;
  std::vector<int> ids_b;
  if (my_file.is_open())
  {
    while(getline(my_file, line)) {
      const string delimiter = "   ";
      std::vector<std::string> tokens = split(line, delimiter);
      int a = stoi(tokens[0]);
      int b = stoi(tokens[1]);
      ids_a.push_back(a);
      ids_b.push_back(b);
    }
    my_file.close();
  }

  else cout << "Unable to open file";

  int total_diff = 0; // part 1
  int sim_score = 0;  // part 2
  // part 1 heap sort
  ranges::make_heap(ids_a);
  ranges::make_heap(ids_b);
  // part 2 tracking
  std::unordered_map<unsigned, size_t> count_in_b;
  for (int b : ids_b) {
    count_in_b[b]++;
  }

  while (!ids_a.empty()) {
    // part 1
    ranges::pop_heap(ids_a);
    int a = ids_a.back();
    ids_a.pop_back();

    ranges::pop_heap(ids_b);
    int b = ids_b.back();
    ids_b.pop_back();

    total_diff += abs(a - b);

    // part 2
    if (count_in_b[a] > 0) {
      sim_score += a * static_cast<int>(count_in_b[a]);
    }
  }

  cout << "Total diff: " << total_diff << endl;
  cout << "Sim score: " << sim_score << endl;

  return 0;
}