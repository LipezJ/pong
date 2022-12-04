#include <iostream>
#include <conio.h>
#include <windows.h>
#include <cstdlib>
#include <vector> 
#include <map>

using namespace std;

vector<int> area1(20, 0);
map<char, int> movimientos_area;

int timed_input(){
	int key = 0;
	if (_kbhit()){
		key = _getch();
	}
	return key;
}
void imprimir(){
	//system("cls");
	int cen = 20;
	for (int i = 0; i < 20; i++) {
		cout<<(area1[i] == 1?"|":" ")<<endl;
	}
	Sleep(100);
}
void mover(vector<int> actual, int key){
    area1[actual[0]] = 0;
    area1[actual[1]] = 0;
    area1[actual[0]+movimientos_area[key]] = 1;
    area1[actual[1]+movimientos_area[key]] = 1;
}
vector<int> area_pos(){
	for (int i = 0; i < area1.size();  i++){
		if (area1[i] == 1) return {i, i+1};
	}
}

int main(){
    int key = 0, k = 0;
    vector<int> actual_area;
    system("mode con: cols=81 lines=21");
    movimientos_area.insert(make_pair(119, -1));
	movimientos_area.insert(make_pair(100, 1));
    
    area1[9] = 1;
    area1[10] = 1;
    while (key != 113){
        actual_area = area_pos();
        key = timed_input();
        if (key == 113) break;
        if (key == 119 and actual_area[0] > 0){
            mover(actual_area, 119);
        }
        if (key == 100 and actual_area[1] < 19){
            mover(actual_area, 100);
        }
        k++;
        if (k == 1000) system("cls");
        imprimir();
    }
    return 0;
}