#include <iostream>
#include <conio.h>
#include <ctime>
#include <windows.h>
#include <vector>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <string>

#define TIME 100

using namespace std;

int tablero[2] = {15, 40};

int movimientos[4][2] = {{-1,-1},{-1,1},{1,1},{1,-1}};
int movimientos__[4] = {2, 3, 0, 1};

map<vector<int>, int> movimientos_ = {
    {{-1,-1}, 0}, {{-1,1}, 1},
    {{1,-1}, 3}, {{1,1}, 2},
    {{0,0}, 4}
};
map<int, int> movimientos_area = {
    {119, -1}, {100, 1},
    {107, -1}, {109, 1}
};

int timed_input();
vector<int> posibilidades_(vector<int> actual);
void reinicio(vector<int> &nuevo, vector<int> &actual);
void imprimir(vector<int> actual, vector<int> puntos, vector<int> actual1, vector<int> actual2);

int main() {
    srand(time(NULL));

    vector<int> actual_rows1 = {tablero[0] / 2, tablero[0] / 2 + 1};
    vector<int> actual_rows2 = {tablero[0] / 2, tablero[0] / 2 + 1};
    vector<int> nuevo = {rand() % tablero[0], tablero[1] / 2};
    vector<int> actual = nuevo;
    vector<int> anterior;
    vector<int> puntos = {0, 0};
    vector<int> posibilidades;

    int tipo, key, posibilidad;

    system("cls");

    while(true) {
        anterior = actual;
        actual = nuevo;

        tipo = movimientos_[{actual[0]-anterior[0], actual[1]-anterior[1]}];

        posibilidades = posibilidades_(actual);

        //movimiento de los jugadores
        key = timed_input();
        if (key == 113) {
            return 0;
        }else if (key == 112) system("pause>nul");
        if ((key == 119 && actual_rows1[0] > 0) || (key == 100 && actual_rows1[1] < tablero[0])){
            actual_rows1[0] = actual_rows1[0] + movimientos_area[key];
            actual_rows1[1] = actual_rows1[1] + movimientos_area[key];
        } else if ((key == 107 && actual_rows2[0] > 0) || (key == 109 && actual_rows2[1] < tablero[0])){
            actual_rows2[0] = actual_rows2[0] + movimientos_area[key];
            actual_rows2[1] = actual_rows2[1] + movimientos_area[key];
        }

        //puntos
        if (puntos[0] == 20){
            system("cls");
            cout<<"Gano el jugador 1"<<endl;
            system("pause>nul");
            return 0;
        } else if (puntos[1] == 20){
            system("cls");
            cout<<"Gano el jugador 2"<<endl;
            system("pause>nul");
            return 0;
        }

        //movimiento de la pelota
            //primer movimiento
        if (actual == anterior){
            posibilidad = posibilidades[rand() % posibilidades.size()];
            nuevo[0] = actual[0] + movimientos[posibilidad][0];
            nuevo[1] = actual[1] + movimientos[posibilidad][1];
        } 
            // esquinas
        else if (posibilidades[0] == 4) {
            if (((actual[0] == actual_rows1[0] || actual[0] == actual_rows1[1]) && (tipo == 0 || tipo == 3)) || ((actual_rows2[0] == actual[0] || actual_rows2[1] == actual[0]) && (tipo == 1 || tipo == 2))) {
                nuevo = anterior;
            } else if (!(actual_rows2[0] == actual[0] || actual_rows2[1] == actual[0])){
                reinicio(nuevo, actual);
                puntos[0] ++;
            } else if (!(actual_rows1[0] == actual[0] || actual_rows1[1] == actual[0])){
                reinicio(nuevo, actual);
                puntos[1] ++;
            }
        }
            //movimiento normal
        else if (posibilidades.size() == 4){
            nuevo[0] = actual[0] + (actual[0] - anterior[0]);
            nuevo[1] = actual[1] + (actual[1] - anterior[1]);
            Sleep(0);
        } 
            //movimiento con pared
        else if (posibilidades == vector<int>{1,2} && !(actual_rows1[0] == actual[0] || actual_rows1[1] == actual[0])){
            reinicio(nuevo, actual);
            puntos[1] ++;
        } else if (posibilidades == vector<int>{0,3} && !(actual_rows2[0] == actual[0] || actual_rows2[1] == actual[0])){
            reinicio(nuevo, actual);
            puntos[0] ++;
        }
            //rebotes
        else {
            if (posibilidades == vector<int>{1,2}){
                if (actual_rows1[0] == actual[0]) {
                    tipo = 0;
                } else if (actual_rows1[1] == actual[0]) {
                    tipo = 3;
                }
            }
            if (posibilidades == vector<int>{0,3}){
                if (actual_rows2[0] == actual[0]) {
                    tipo = 1;
                } else if (actual_rows2[1] == actual[0]) {
                    tipo = 2;
                }
            }
            Sleep(0);
            posibilidades.erase(remove(posibilidades.begin(), posibilidades.end(), movimientos__[tipo]), posibilidades.end());
            nuevo[0] = actual[0] + movimientos[posibilidades[0]][0];
            nuevo[1] = actual[1] + movimientos[posibilidades[0]][1];
        }
        imprimir(nuevo, puntos, actual_rows1, actual_rows2);
    }
    return 0;
}

//calcular posibilidades
vector<int> posibilidades_(vector<int> actual){
    if ((actual[0] == 0 && actual[1] == 0) || (actual[0] == 0 && actual[1] == tablero[1]) || (actual[0] == tablero[0] && actual[1] == 0) || (actual[0] == tablero[0] && actual[1] == tablero[1])){
        return vector<int>{4};
    }
    if (actual[0] == tablero[0]){
        return vector<int>{0, 1};
    } else if (actual[0] == 0){
        return vector<int>{2, 3};
    } else if (actual[1] == tablero[1]){
        return vector<int>{0, 3};
    } else if (actual[1] == 0){
        return vector<int>{1, 2};
    } else {
        return vector<int>{0, 1, 2, 3};
    }
}

//input de teclas
int timed_input(){
    int key = 0;
	if (_kbhit()){
		key = _getch();
	}
	return key;
}

//reinicio de la pelota
void reinicio(vector<int> &nuevo, vector<int> &actual){
    nuevo[0] = rand() % tablero[0];
    nuevo[1] = tablero[1] / 2;
    actual = nuevo;
    Sleep(200);
}

//imprimir tablero
void imprimir(vector<int> actual, vector<int> puntos, vector<int> actual1, vector<int> actual2){
    printf("\x1b[0;0H");
    for (int i = 0; i < tablero[1]+3; i++) cout<<"x";
    cout<<"\n";
	for (int i = 0; i < tablero[0]+1; i++) {
        if (i == actual1[0] || i == actual1[1]) cout<<"|";
        else cout<<" ";
        for (int j = 0; j < tablero[1]+1; j++){
            if (j == actual[1] && i == actual[0]) {
                cout<<"O";
            } else cout<<" ";
        }
        if (i == actual2[0] || i == actual2[1]) cout<<"|";
        else cout<<" ";
        cout<<"\n";
	}
    for (int i = 0; i < tablero[1]+3; i++) cout<<"x";
    cout<<"\n"<<puntos[0]<<" - "<<puntos[1]<<endl;
	Sleep(TIME);
}