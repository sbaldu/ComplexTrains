
#pragma once

#include <string>
#include <vector>

class Train {
  private:
	int m_station;
	bool m_prioritary;
	std::string m_id;
	std::vector<std::string> m_itinerary;
	
  public:
	Train() = default;
	Train(int station, bool prioritary)
	  : m_station{station}, m_prioritary{prioritary} {}
	Train(int station, bool prioritary, std::vector<std::string> itinerary)
	  : m_station{station}, m_prioritary{prioritary}, m_itinerary{std::move(itinerary)} {}

	const int station() const {
	  return m_station;
	}
	void set_station(int station) {
	  m_station = station;
	}

	const bool prioritary() const {
	  return m_prioritary;
	}
	void set_priority(bool prioritary) {
	  m_prioritary = prioritary;
	}

	const std::string id() const {
	  return m_id;
	}
	void set_id(std::string id) {
	  m_id = id;
	}

	const std::vector<std::string>& itinerary() const {
	  return m_itinerary;
	}
	void set_itinerary(std::vector<std::string> itinerary) {
	  m_itinerary = std::move(itinerary);
	}
	void add_to_itinerary(const std::string& station) {
	  m_itinerary.push_back(station);
	}

	void move(int next_station, bool station_available) {
	  if (station_available) {
		m_station = next_station;
	  }
	}
	
};
