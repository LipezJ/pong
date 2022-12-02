#include <iostream>
#include <conio.h>
#include <windows.h>
#include <cstdlib>
#include <vector> 
#include <map>
#include <time.h>

using namespace std;

vector<vector<int>> tablero(20, vector<int> (80, 0));
vector<int> area1(20, 0), area2(20, 0), posibilidades;
map<char, int> movimientos_area;
map<vector<int>, int> movimientos_;
int movimientos[4][2] = {{-1,-1},{-1,1},{1,1},{1,-1}};
int movimientos__[4] = {2, 3, 0, 1}, time_;

void imprimir(int p1, int p2){
	system("cls");
	for (int i = 0; i < 20; i++) {
		cout<<(area1[i] == 1?"|":" ");
		for (int j = 0; j < 80; j++){
            if (tablero[i][j] == 1) {
                cout<<"O";
            } else if (j == 37 and i == 0) cout<<p1;
            else if (j == 40 and i == 0) cout<<p2; 
            else cout<<" ";
        }
		cout<<(area2[i] == 1?"|":" ")<<endl;
	}
	Sleep(time_);
}
void mover(vector<int> actual, int key, int t){
    if (t == 1){
        area1[actual[0]] = 0;
        area1[actual[1]] = 0;
        area1[actual[0]+movimientos_area[key]] = 1;
        area1[actual[1]+movimientos_area[key]] = 1;
    } else if (t == 2) {
        area2[actual[0]] = 0;
        area2[actual[1]] = 0;
        area2[actual[0]+movimientos_area[key]] = 1;
        area2[actual[1]+movimientos_area[key]] = 1;
    }
}
vector<int> area_pos(vector<int> area){
	for (int i = 0; i < area1.size();  i++){
		if (area[i] == 1) return {i, i+1};
	}
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
int timed_input(){
	int key = 0;
	if (_kbhit()){
		key = _getch();
	}
	return key;
}
vector<int> random(vector<int> actual){
	tablero[actual[0]][actual[1]] = 0;
	int inicio_fila = (rand() % 18) + 1;
	tablero[inicio_fila][39] = 1;
	return {inicio_fila, 39};
}

int main(){
    cout<<"velocidad: ";
    cin>>time_;
    srand(time(NULL));
    system("mode con: cols=82 lines=22");
    movimientos_.insert(make_pair(make_vector(-1,-1), 0));
	movimientos_.insert(make_pair(make_vector(-1,1), 1));
	movimientos_.insert(make_pair(make_vector(1,1), 2));
	movimientos_.insert(make_pair(make_vector(1,-1), 3));
	movimientos_.insert(make_pair(make_vector(0,0), 4));
    movimientos_area.insert(make_pair(119, -1));
	movimientos_area.insert(make_pair(100, 1));
    movimientos_area.insert(make_pair(107, -1));
	movimientos_area.insert(make_pair(109, 1));

    Sleep(200);

    int key, inicio  = (rand() % 18)+1, puntos1 = 0, puntos2 = 0, tipo, tipo_;
	vector<int> actual = make_vector(inicio, 40), anterior, nuevo, actual_area1, actual_area2, nue(2);
    bool k = true;

    area1[9] = 1;
    area1[10] = 1;
    area2[9] = 1;
    area2[10] = 1;

    tablero[inicio][40] = 1;
    
    while(puntos1 < 6 or puntos2 < 6){
        if (!k) {
            tablero[actual[0]][actual[1]] = 0;
            tablero[(rand() % 17)+2][40] = 1;
            actual = buscar_uno();
            nue = actual;
            k = true;
        }
        while (k){
            anterior = actual;
            actual = buscar_uno();

            for (auto x: anterior) cout<<x;
            cout<<" ";
            for (auto x: actual) cout<<x;
            cout<<" ";
            for (auto x: nue) cout<<x;

            tipo = movimientos_[{actual[0]-anterior[0], actual[1]-anterior[1]}];
            posibilidades = posibilidades_(actual);

            actual_area1 = area_pos(area1);
            actual_area2 = area_pos(area2);

            key = timed_input();
            if (key == 113) {
                return 0;
            }else if (key == 112) system("pause>nul");

            if ((key == 119 and actual_area1[0] > 0) or (key == 100 and actual_area1[1] < 19)){
                mover(actual_area1, key, 1);
            } else if ((key == 107 and actual_area2[0] > 0) or (key == 109 and actual_area2[1] < 19)){
                mover(actual_area2, key, 2);
            }

            if (puntos1 == 20){
                system("cls");
                cout<<"Ganaste, jugador 1";
                Sleep(1000);
                break;
                system("cls");
            }else if (puntos2 == 20) {
                system("cls");
                cout<<"Ganaste, jugador 2";
                Sleep(1000);
                break;
                system("cls");
            }

            if (actual == anterior){
                int posibilidades__ = posibilidades_(actual)[rand() % posibilidades_(actual).size()];
                nuevo = {actual[0] + movimientos[posibilidades__][0], movimientos[posibilidades__][1] + actual[1]};
                
            }else if (posibilidades[0] == 4){
                if (actual[0] == actual_area1[0] or actual[0] == actual_area2[1]){
                    nuevo = anterior;
                }else if(!(actual[0] == actual_area1[0] or actual[0] == actual_area2[1])){
                    puntos2 ++;
                    Sleep(500);
                    k = false;
                    cout<<k;
                    continue;
                }else if(!(actual[0] == actual_area2[0] or actual[0] == actual_area2[1])){
                    puntos1 ++;
                    Sleep(500);
                    k = false;
                    cout<<k;
                    continue;
                }
            }else if(posibilidades.size() == 4){
                nuevo = {actual[0] + (actual[0] - anterior[0]), actual[1] + (actual[1] - anterior[1])};
                
            }else if(posibilidades == make_vector(1,2) and !(actual_area1[0] == actual[0] or actual_area1[1] == actual[0])){
                puntos2 ++;
                Sleep(500);
                k = false;
                cout<<k;
                continue;
            }else if(posibilidades == make_vector(0,3) and !(actual_area2[0] == actual[0] or actual_area2[1] == actual[0])){
                puntos1 ++;
                Sleep(500);
                k = false;
                cout<<k;
                continue;
            }else{
                if(posibilidades == make_vector(1,2)){
                    if (actual_area1[0] == actual[0]){
                        tipo = 0;
                    }else if (actual_area1[1] == actual[0]){
                        tipo = 3;
                    }
                }
                if(posibilidades == make_vector(0,3)){
                    if (actual_area2[0] == actual[0]){
                        tipo = 1;
                    }else if (actual_area2[1] == actual[0]){
                        tipo = 2;
                    }
                }
                tipo_ = movimientos__[tipo];
                remove(tipo_);
                nuevo = {actual[0] + movimientos[posibilidades[0]][0], actual[1] + movimientos[posibilidades[0]][1]};
            }
            tablero[actual[0]][actual[1]] = 0;
            tablero[nuevo[0]][nuevo[1]] = 1;
            imprimir(puntos1, puntos2);
        }
    }
    return 0;
}