
#pragma once

#include <vector>

class Train {
  private:
	int m_station;
	bool m_prioritary;
	std::vector<int> m_itinerary;
	
  public:
	Train() = default;
	Train(int station, bool prioritary)
	  : m_station{station}, m_prioritary{prioritary} {}
	Train(int station, bool prioritary, std::vector<int> itinerary)
	  : m_station{station}, m_prioritary{prioritary}, m_itinerary{std::move(itinerary)} {}

	const int station() const {
	  return m_station;
	}
	const bool prioritary() const {
	  return m_prioritary;
	}
	const std::vector<int>& itinerary() const {
	  return m_itinerary;
	}

	void move(int next_station, bool station_available) {
	  if (station_available) {
		m_station = next_station;
	  }
	}
	
	void set_itinerary(std::vector<int> itinerary) {
	  m_itinerary = std::move(itinerary);
	}

	void add_to_itinerary(int station) {
	  m_itinerary.push_back(station);
	}
};
