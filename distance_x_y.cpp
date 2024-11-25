#include <iostream>
#include <cmath>
using namespace std;
double distance2(double x, double y, double x1, double y1)
{
  double f;
  f = sqrt((x - x1)*(x - x1) + (y - y1)*(y - y1));
  return f;
}
int main() {
  double x, y, x1, y1, f;
  cin >> x >> y >> x1 >> y1;
  f = distance2(x, y, x1, y1);
  cout << f;
  return 0;
}