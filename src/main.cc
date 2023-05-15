
#include <fstream>
#include <sstream>

#include "CXXGraph.hpp"

#include "station.hpp"
#include "train.hpp"

int main() {
  // Construct the list of trains
  int n_trains{};
  std::vector<Train> list_of_trains;

  // Import the trains from file
  std::ifstream train_file("../data/trains.csv");
  std::string file_row;
  std::string priority;
  std::string train_id;
  std::string train_stop;
  while (getline(train_file, file_row)) {
    std::stringstream row_stream(file_row);

    Train t;
    // Read the priority
    getline(row_stream, priority, ',');
    if (priority == "Frecciarossa" && priority == "Frecciabianca" && priority == "Frecciaargento") {
      t.set_priority(true);
    } else {
      t.set_priority(false);
    }
    // Read the train id
    getline(row_stream, train_id, ',');
    t.set_id(train_id);
    // Read the elements of the itinerary
    while (getline(row_stream, train_stop, ',')) {
      // Clean the string
      train_stop.erase(std::remove(train_stop.begin(), train_stop.end(), ' '), train_stop.end());
      train_stop.erase(std::remove(train_stop.begin(), train_stop.end(), '"'), train_stop.end());
      train_stop.erase(std::remove(train_stop.begin(), train_stop.end(), '['), train_stop.end());
      train_stop.erase(std::remove(train_stop.begin(), train_stop.end(), ']'), train_stop.end());
      train_stop.erase(std::remove(train_stop.begin(), train_stop.end(), '\''), train_stop.end());
      // Add to the itinerary
      t.add_to_itinerary(train_stop);
    }
    list_of_trains.push_back(t);
    ++n_trains;
  }

  // Construct the graph where the nodes are stations
  CXXGraph::Graph<Station> graph;
  graph.readFromDotFile("../data", "stations");
}
