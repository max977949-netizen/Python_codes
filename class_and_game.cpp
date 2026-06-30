#include <iostream>
#include <cstdlib>
#include <ctime>
using std::cout;
using std::endl;
using std::cin;

class People {
private:
	int life;
	int dano;
public:
	People(int a, int c) {
		life = a;
		life = life > 100? 100:life;
		dano = c;
		dano = dano > 25? 25:dano;
	}

	int getLife() {
		return life;
	}
	int getDano() {
		return dano;
	}

	void sertar(People &objetivo) {
		objetivo.life -= dano;
		objetivo.life = objetivo.life <= 0? 0:objetivo.life;
		cout<<"El enemigo tiene "<<objetivo.life<<endl;
		if(objetivo.life > 0) {
			life -= objetivo.dano;
			life = life < 0? 0:life;
			cout<<"Tienes "<<life<<endl;
		}

	}
	void masur(People &enemigo, int z) {
		int y = life + z;
		life = y > 100? 100:y;
		cout<<"Te curaste "<<z<<" Y tienes "<<life<<"PS"<<endl;
		enemigo.life = enemigo.life < 25? enemigo.life + 50:enemigo.life;
		cout<<"El enemigo se curo 50 y tiene "<<enemigo.life<<"PS"<<endl;

	}


};
int main() {
	int des;
	int w;
	srand(time(NULL));
	int g = (rand() % (100 - 50 + 1)) + 50;
	int h = (rand() % (25 - 10 + 1)) + 20;
	People A1(g, h);
	h = (rand() % (25 - 10 + 1)) + 20;
	g = (rand() % (100 - 50 + 1)) + 50;
	People B2(g, h);
	cout<<"Tienes "<<A1.getLife()<<"PS y "<<A1.getDano()<<"PD"<<endl;
	cout<<"Tiene el enemigo "<<B2.getLife()<<"PS y "<<B2.getDano()<<"PD"<<endl;
	while(A1.getLife() > 0 && B2.getLife() > 0) {
		cout<<"Que acción quieres 1.- atacar: 2.-curarse"<<endl;
		cin>>des;
		switch(des) {
		case 1:
			A1.sertar(B2);
			break;
		case 2:
			cout<<"Cuanto te quieres curar? "<<endl;
			cin>>w;
			A1.masur(B2, w);
			break;
		default:
			cout<<"Accion invalida "<<endl;
			break;
		}
	}
	return 0;
}
