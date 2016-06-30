//input: vector<vector<string>> map //"line1, stn1, stn2, ..." "line2, stn1, stn2, ..."
//output: a graph that connect stations
//map[i][0] -- line name; map[i][j] -- station name

#include<iostream>
#include<vector>
#include<queue>
#include<unordered_map>
#include<unordered_set>
// #include<string>
// #include<sstream>
// #define n 7 //no. of lines
using namespace std;

vector<vector<string>> metro = {{"山手線","品川","大崎","五反田","目黒","恵比寿","渋谷","原宿","代々木","新宿","新大久保","高田馬場","目白","池袋","大塚","巣鴨","駒越","田端駅","西日暮里","日暮里","鶯谷","上野","御徒町","秋葉原","神田","東京","有楽町","新橋","浜松町","田町","品川"},

{"東横線","横浜","反町","東白楽","白楽","妙蓮寺","菊名","大倉山","綱島","日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","自由が丘","都立大学","学芸大学","祐天寺","中目黒","代官山","渋谷"},

{"目黒線","日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","奥沢","大岡山","洗足","西小山","武蔵小山","不動前","目黒"},

{"池上線","蒲田","蓮沼","池上","千鳥町","久が原","御嶽山","雪が谷大塚","石川台","洗足池","長原","旗の台","荏原中延","戸越銀座","大崎広小路","五反田"},

{"多摩川線","多摩川","沼部","鵜の木","下丸子","武蔵新田","矢口渡","蒲田"},

{"大井町線","二子玉川","上野毛","等々力","尾山台","九品仏","自由が丘","緑が丘","大岡山","北千束","旗の台","荏原町","中延","戸越公園","下神明","大井町"},

{"日比谷線","中目黒","恵比寿","広尾","六本木","神谷町","霞ケ関","日比谷","銀座","東銀座","築地","八丁堀","茅場町","人形町","小伝馬町","秋葉原","仲御徒町","上野","入谷","三ノ輪","南千住","北千住"}};

unordered_map<string, vector<string>> graph; //relation btw stns
unordered_map<string, vector<string>> stn_line; //match stns and lines
string start, to; //start and end point

void MakeGraph(vector<vector<string>> metro){

	//constrcut stn_line
	for(int i = 0; i < metro.size(); i++){
		string line = metro[i][0];
		for(int j = 1; j < metro[i].size(); j++){
			if(metro[i][j] == "品川" && j > 1) continue; //Shinagawa appeared twice because Yamanote is a circle line
			stn_line[metro[i][j]].push_back(line);
		}
	}
	//construct graph
	for(int i = 0; i < metro.size(); i++){
		for(int j = 1; j < metro[i].size(); j++){
			if(j == 1) graph[metro[i][j]].push_back(metro[i][j+1]);
			else if(j == metro[i].size()-1) graph[metro[i][j]].push_back(metro[i][j-1]);
			else {
				graph[metro[i][j]].push_back(metro[i][j+1]);
				graph[metro[i][j]].push_back(metro[i][j+1]);
			}
		}
	}

}

bool bfs(){

	nordered_set<string> visited;
	unordered_map<string, string> from;
	unordered_map<string, int> dis;
	queue<string> q;

	string curr = start;
	q.push(curr);
	dis[curr] = 0;

	while(!q.empty()){
		curr = q.front(); q.pop();
		visited.insert(curr);
		for(int i = 0; i < graph[curr].size(); i++){
			if(visited.find(graph[curr][i]) != visited.end()) continue;
			q.push(graph[curr][i]);
			from[graph[curr][i]] = curr;
			dis[graph[curr][i]] = dis[curr]+1;
			visited.insert(graph[curr][i]);
			if(graph[curr][i] == to) return true;
		}

	}

	return false;

}

vector<string> FindPath(){

	vector<string> path;

	if(!bfs()) path.push_back("No route found T.T");

	else {
		string temp = to;
		path.push_back(temp);
		while(temp != start){
			path.push_back(from[temp]);
			temp = from[temp];
		}

	}

	return path;
	
}

int main(){

	// vector<string> line;
	// string s;
	// for(int i = 0; i < n; i++){
	// 	getline(cin, s);
	// 	stringstream ss(s);
	// 	string stn_name;
	// 	while(ss >> stn_name) line.push_back(stn_name);
	// 	map.push_back(line);
	// }

	MakeGraph(metro);

	cin >> start >> to;

	vector<string> res = FindPath();

    for(int i = res.size() - 1; i >= 0; i--){
        cout << res[i];
        for(int j = 0; j < stn_line[res[i]].size(); j++){
            cout << "(" << stn_line[res[i]][j] << ")";
        }
        cout << endl;
    }

	return 0;
}