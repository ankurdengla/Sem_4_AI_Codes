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

void printPath(int val) {
	if(val == -1) {
		return;
	}
	printPath(m[val]);
	cout << endl;
	printVal(val);
}

void solve() {
	int dest = 123456780;
	node p;
	p = init(p);
	int ni = findVal(p.adj);
	s.insert(ni);
	m[ni] = -1;
	queue<node> q;
	q.push(p);
	while(!q.empty()) {
		node p = q.front();
		q.pop();
		int prev = findVal(p.adj);
		cout << prev << endl;
		if(prev == dest) {
			break;
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
				q.push(p);
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
				q.push(p);
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
				q.push(p);
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
				q.push(p);
			}
			temp = p.adj[id.ff][id.ss];
			p.adj[id.ff][id.ss] = p.adj[id.ff][id.ss + 1];
			p.adj[id.ff][id.ss + 1] = temp;
		}
	}
	if(m.find(dest) == m.end()) {
		cout << "No solution\n";
	}
	else {
		printPath(dest);
	}
}

int main() {
	solve();
	return 0;
}