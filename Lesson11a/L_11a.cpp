#include <iostream>
using namespace std;

class OfficeItem{
protected:
	int count;
public:
	OfficeItem();
	int UseUpOne();
	void Restock(int HowMany);
};

OfficeItem::OfficeItem() {
	count = 0;
}

int OfficeItem::UseUpOne() {
	count--;
	return count;
}

void OfficeItem::Restock(int HowMany) {
	count += HowMany;
}

int main()
{
	OfficeItem inst;
	inst.Restock(15);
	cout << inst.UseUpOne() << endl;
	return 0;
}