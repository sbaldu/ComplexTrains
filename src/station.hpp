
#pragma one

#include <ostream>
#include <vector>

constexpr int default_delay{5};

class Station {
  private:
	int m_capacity;
	int m_delay;
	std::vector<int> m_queue;
	
  public:
	Station() = default;
	Station(int capacity) : m_capacity{capacity}, m_delay{default_delay} {}
	Station(int capacity, int delay) : m_capacity{capacity}, m_delay{delay} {}

	const int capacity() const { return m_capacity; }
	const int delay() const { return m_delay; }
	const std::vector<int>& queue() const { return m_queue; }

	void set_queue(std::vector<int> queue) {
	  m_queue = std::move(queue);
	}
	void add_to_queue(int train) {
	  m_queue.push_back(train);
	}

	// Overload istream operator
	friend std::istream& operator>>(std::istream& is, Station& station) {
	  is >> station.m_capacity;
	  is >> station.m_delay;
	  return is;
	}
	// Overload ostream operator
	friend std::ostream& operator<<(std::ostream& os, Station const& station) {
	  os << "Capacity=" << station.m_capacity << ", Delay=" << station.m_delay << "\n";
	  return os;
	}
};

