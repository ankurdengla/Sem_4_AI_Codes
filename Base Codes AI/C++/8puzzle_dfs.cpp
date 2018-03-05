#include <bits/stdc++.h>
#define mp make_pair
#define ff first
#define ss second
using namespace std;
typedef pair<int, int> ipair;
set<int> s;
map<int, int> m;
struct node {
	int adj[3][3];
};
int dest = 123456780;

node init(node p) {
	p.adj[0][0] = 0;
	p.adj[0][1] = 2;
	p.adj[0][2] = 3;
	p.adj[1][0] = 1;
	p.adj[1][1] = 4;
	p.adj[1][2] = 5;
	p.adj[2][0] = 7;
	p.adj[2][1] = 8;
	p.adj[2][2] = 6;
	return p;
}

int findVal(int mat[][3]) {
	int ans = 0;
	int i, j;
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			ans = ans * 10 + mat[i][j];
		}
	}
	return ans;
}

void printMat(int mat[][3]) {
	int i, j;

	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			cout << mat[i][j] << " ";
		}
		cout << endl;
	}
}

void printVal(int val) {
	int temp[3][3];
	int i, j;
	for(i = 2; i >= 0; i--) {
		for(j = 2; j >= 0; j--) {
			temp[i][j] = val%10;
			val/=10;
		}
	}
	printMat(temp);
}

ipair findId(int mat[][3]) {
	int i, j;
	for(i = 0; i < 3; i++) {
		for(j = 0; j < 3; j++) {
			if(mat[i][j] == 0) {
				return mp(i, j);
			}
		}
	}
}

int valid(int mat[][3]) {
	int val = findVal(mat);
	return (s.find(val) == s.end());
}

int c = 0;
void printPath(int val) {
	if(val == -1) {
		return;
	}
	printPath(m[val]);
	cout << endl;
	printVal(val);
}
int solve(node p, int prev) {
	if(c < 30) {
		cout << prev << endl;
		c++;
	}
	if(prev == dest) {
		printPath(dest);
		return 1;
	}
	ipair id = findId(p.adj);
	if(id.ff) {
		int temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff - 1][id.ss];
		p.adj[id.ff - 1][id.ss] = temp;
		if(valid(p.adj)) {
			int nw = findVal(p.adj);
			m[nw] = prev;
			s.insert(nw);
			if(solve(p, nw)) {
				return 1;
			}
		}
		temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff - 1][id.ss];
		p.adj[id.ff - 1][id.ss] = temp;
	}
	if(id.ff < 2) {
		int temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff + 1][id.ss];
		p.adj[id.ff + 1][id.ss] = temp;
			if(valid(p.adj)) {
			int nw = findVal(p.adj);
			m[nw] = prev;
			s.insert(nw);
			if(solve(p, nw)) {
				return 1;
			}
		}
		temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff + 1][id.ss];
		p.adj[id.ff + 1][id.ss] = temp;
	}
	if(id.ss) {
		int temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff][id.ss - 1];
		p.adj[id.ff][id.ss - 1] = temp;
		if(valid(p.adj)) {
			int nw = findVal(p.adj);
			m[nw] = prev;
			s.insert(nw);
			if(solve(p, nw)) {
				return 1;
			}
		}
		temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff][id.ss - 1];
		p.adj[id.ff][id.ss - 1] = temp;
	}
	if(id.ss < 2) {
		int temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff][id.ss + 1];
		p.adj[id.ff][id.ss + 1] = temp;
		if(valid(p.adj)) {
			int nw = findVal(p.adj);
			m[nw] = prev;
			s.insert(nw);
			if(solve(p, nw)) {
				return 1;
			}
		}
		temp = p.adj[id.ff][id.ss];
		p.adj[id.ff][id.ss] = p.adj[id.ff][id.ss + 1];
		p.adj[id.ff][id.ss + 1] = temp;
	}
	return 0;
}

int main() {
	node p;
	p = init(p);
	int ni = findVal(p.adj);
	m[ni] = -1;
	s.insert(ni);
	int ans = solve(p, ni);
	if(!ans) {
		cout << "No solution\n";
	}
	return 0;
}