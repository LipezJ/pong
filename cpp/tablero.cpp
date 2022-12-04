#include <iostream>
#include <conio.h>
#include <windows.h>
#include <cstdlib>
#include <vector> 
#include <map>
#include <time.h>

using namespace std;

vector<vector<int>> tablero(20, vector<int> (80, 0));
map<vector<int>, int> movimientos_;
vector<int> posibilidades;
int movimientos[4][2] = {{-1,-1},{-1,1},{1,1},{1,-1}};
int movimientos__[4] = {2, 3, 0, 1}, time_;

int timed_input(){
	int key = 0;
	if (_kbhit()){
		key = _getch();
	}
	return key;
}
void imprimir(){
	int cen = 39;
    system("cls");
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 80; j++){
            if (tablero[i][j] == 1) {
                cout<<"O";
            } else cout<<" ";
        };
        cout<<endl;
	}
	Sleep(time_);
}
vector<int> make_vector(int a, int b){
	return {a, b};
}
vector<int> buscar_uno(){
	for (int i = 0; i < 20; i++){
		for (int j = 0; j < 80; j++) {
			if (tablero[i][j] == 1) return {i, j};
		}
	}
	return {0,0};
}
vector<int> posibilidades_(vector<int> actual){
	if ((actual[0] == 0 and actual[1] == 0) or (actual[0] == 0 and actual[1] == 79 or (actual[0] == 19 and actual[1] == 0) or (actual[0] == 19 and actual[1] == 79))) {
        return {4,0,1};
    }else if (actual[0] == 19){
		return {0,1};
	}else if (actual[0] == 0){
		return {2,3};
	}else if (actual[1] == 79){
		return {0,3};
	}else if (actual[1] == 0){
		return {1,2};
	}else{
		return {1,2,3,4};
	}
}
int remove(int item){
	for (int i = 0; i < posibilidades.size(); i++){
		if (posibilidades[i] == item){
            posibilidades.erase(posibilidades.begin()+i, posibilidades.begin() + (i+1)); 
        };
	}
	return 10;
}

int main(){
    cin>>time_;
    srand(time(NULL));
    system("mode con: cols=80 lines=22");
    movimientos_.insert(make_pair(make_vector(-1,-1), 0));
	movimientos_.insert(make_pair(make_vector(-1,1), 1));
	movimientos_.insert(make_pair(make_vector(1,1), 2));
	movimientos_.insert(make_pair(make_vector(1,-1), 3));
	movimientos_.insert(make_pair(make_vector(0,0), 4));

    int key, inicio_fila = rand() % 20, puntos1 = 0, puntos2 = 0, tipo, tipo_;
	vector<int> actual = make_vector(inicio_fila, 39);
	vector<int> anterior, nuevo;

    tablero[inicio_fila][39] = 1;

    imprimir();

    while (true){
        anterior = actual;
        actual = buscar_uno();
        tipo = movimientos_[{actual[0]-anterior[0], actual[1]-anterior[1]}];
		posibilidades = posibilidades_(actual);
        key = timed_input();
		if (key == 113) {
            return 0;
        }else if (key == 112) system("pause>nul");
        if (actual == anterior){
			int posibilidades__ = posibilidades[rand() % posibilidades.size()];
			nuevo = {actual[0] + movimientos[posibilidades__][0], actual[1] + movimientos[posibilidades__][1]};
            
		}else if (posibilidades[0] == 4){
            nuevo = anterior;
		}else if(posibilidades.size() == 4){
			nuevo = {actual[0] + (actual[0] - anterior[0]), actual[1] + (actual[1] - anterior[1])};
            
		}else{
			tipo_ = movimientos__[tipo];
			remove(tipo_);
            nuevo = {actual[0] + movimientos[posibilidades[0]][0], actual[1] + movimientos[posibilidades[0]][1]};
            
		}
        tablero[nuevo[0]][nuevo[1]] = 1;
        tablero[actual[0]][actual[1]] = 0;
        imprimir();
    }
}