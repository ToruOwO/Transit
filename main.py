#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import webapp2

class MainPage(webapp2.RequestHandler):

	def get(self):
		self.response.headers["Content-Type"] = "text/html"
		self.response.out.write("""
<html>
	<head>
	<meta charset="utf-8">
		<title>Route</title>
	</head>
	<body>
		<form action="/yay" method="post">
			出発：
			<select name="from">
				
				  <option disabled>山手線</option>
				  
					<option >品川</option>
					
					<option >大崎</option>
					
					<option >五反田</option>
					
					<option >目黒</option>
					
					<option >恵比寿</option>
					
					<option selected>渋谷</option>
					
					<option >原宿</option>
					
					<option >代々木</option>
					
					<option >新宿</option>
					
					<option >新大久保</option>
					
					<option >高田馬場</option>
					
					<option >目白</option>
					
					<option >池袋</option>
					
					<option >大塚</option>
					
					<option >巣鴨</option>
					
					<option >駒越</option>
					
					<option >田端駅</option>
					
					<option >西日暮里</option>
					
					<option >日暮里</option>
					
					<option >鶯谷</option>
					
					<option >上野</option>
					
					<option >御徒町</option>
					
					<option >秋葉原</option>
					
					<option >神田</option>
					
					<option >東京</option>
					
					<option >有楽町</option>
					
					<option >新橋</option>
					
					<option >浜松町</option>
					
					<option >田町</option>
					
					<option >品川</option>
					
				
				  <option disabled>東横線</option>
				  
					<option >横浜</option>
					
					<option >反町</option>
					
					<option >東白楽</option>
					
					<option >白楽</option>
					
					<option >妙蓮寺</option>
					
					<option >菊名</option>
					
					<option >大倉山</option>
					
					<option >綱島</option>
					
					<option >日吉</option>
					
					<option >元住吉</option>
					
					<option >武蔵小杉</option>
					
					<option >新丸子</option>
					
					<option >多摩川</option>
					
					<option >田園調布</option>
					
					<option >自由が丘</option>
					
					<option >都立大学</option>
					
					<option >学芸大学</option>
					
					<option >祐天寺</option>
					
					<option >中目黒</option>
					
					<option >代官山</option>
					
					<option >渋谷</option>
					
				
				  <option disabled>目黒線</option>
				  
					<option >日吉</option>
					
					<option >元住吉</option>
					
					<option >武蔵小杉</option>
					
					<option >新丸子</option>
					
					<option >多摩川</option>
					
					<option >田園調布</option>
					
					<option >奥沢</option>
					
					<option >大岡山</option>
					
					<option >洗足</option>
					
					<option >西小山</option>
					
					<option >武蔵小山</option>
					
					<option >不動前</option>
					
					<option >目黒</option>
					
				
				  <option disabled>池上線</option>
				  
					<option >蒲田</option>
					
					<option >蓮沼</option>
					
					<option >池上</option>
					
					<option >千鳥町</option>
					
					<option >久が原</option>
					
					<option >御嶽山</option>
					
					<option >雪が谷大塚</option>
					
					<option >石川台</option>
					
					<option >洗足池</option>
					
					<option >長原</option>
					
					<option >旗の台</option>
					
					<option >荏原中延</option>
					
					<option >戸越銀座</option>
					
					<option >大崎広小路</option>
					
					<option >五反田</option>
					
				
				  <option disabled>多摩川線</option>
				  
					<option >多摩川</option>
					
					<option >沼部</option>
					
					<option >鵜の木</option>
					
					<option >下丸子</option>
					
					<option >武蔵新田</option>
					
					<option >矢口渡</option>
					
					<option >蒲田</option>
					
				
				  <option disabled>大井町線</option>
				  
					<option >二子玉川</option>
					
					<option >上野毛</option>
					
					<option >等々力</option>
					
					<option >尾山台</option>
					
					<option >九品仏</option>
					
					<option >自由が丘</option>
					
					<option >緑が丘</option>
					
					<option >大岡山</option>
					
					<option >北千束</option>
					
					<option >旗の台</option>
					
					<option >荏原町</option>
					
					<option >中延</option>
					
					<option >戸越公園</option>
					
					<option >下神明</option>
					
					<option >大井町</option>
					
				
				  <option disabled>日比谷線</option>
				  
					<option >中目黒</option>
					
					<option >恵比寿</option>
					
					<option >広尾</option>
					
					<option >六本木</option>
					
					<option >神谷町</option>
					
					<option >霞ケ関</option>
					
					<option >日比谷</option>
					
					<option >銀座</option>
					
					<option >東銀座</option>
					
					<option >築地</option>
					
					<option >八丁堀</option>
					
					<option >茅場町</option>
					
					<option >人形町</option>
					
					<option >小伝馬町</option>
					
					<option >秋葉原</option>
					
					<option >仲御徒町</option>
					
					<option >上野</option>
					
					<option >入谷</option>
					
					<option >三ノ輪</option>
					
					<option >南千住</option>
					
					<option >北千住</option>
					
				
			</select>
			<br>
			到着：
			<select name="to">
				
				  <option disabled>山手線</option>
				  
					<option >品川</option>
					
					<option >大崎</option>
					
					<option >五反田</option>
					
					<option >目黒</option>
					
					<option >恵比寿</option>
					
					<option >渋谷</option>
					
					<option >原宿</option>
					
					<option >代々木</option>
					
					<option >新宿</option>
					
					<option >新大久保</option>
					
					<option >高田馬場</option>
					
					<option >目白</option>
					
					<option >池袋</option>
					
					<option >大塚</option>
					
					<option >巣鴨</option>
					
					<option >駒越</option>
					
					<option >田端駅</option>
					
					<option >西日暮里</option>
					
					<option >日暮里</option>
					
					<option >鶯谷</option>
					
					<option >上野</option>
					
					<option >御徒町</option>
					
					<option selected>秋葉原</option>
					
					<option >神田</option>
					
					<option >東京</option>
					
					<option >有楽町</option>
					
					<option >新橋</option>
					
					<option >浜松町</option>
					
					<option >田町</option>
					
					<option >品川</option>
					
				
				  <option disabled>東横線</option>
				  
					<option >横浜</option>
					
					<option >反町</option>
					
					<option >東白楽</option>
					
					<option >白楽</option>
					
					<option >妙蓮寺</option>
					
					<option >菊名</option>
					
					<option >大倉山</option>
					
					<option >綱島</option>
					
					<option >日吉</option>
					
					<option >元住吉</option>
					
					<option >武蔵小杉</option>
					
					<option >新丸子</option>
					
					<option >多摩川</option>
					
					<option >田園調布</option>
					
					<option >自由が丘</option>
					
					<option >都立大学</option>
					
					<option >学芸大学</option>
					
					<option >祐天寺</option>
					
					<option >中目黒</option>
					
					<option >代官山</option>
					
					<option >渋谷</option>
					
				
				  <option disabled>目黒線</option>
				  
					<option >日吉</option>
					
					<option >元住吉</option>
					
					<option >武蔵小杉</option>
					
					<option >新丸子</option>
					
					<option >多摩川</option>
					
					<option >田園調布</option>
					
					<option >奥沢</option>
					
					<option >大岡山</option>
					
					<option >洗足</option>
					
					<option >西小山</option>
					
					<option >武蔵小山</option>
					
					<option >不動前</option>
					
					<option >目黒</option>
					
				
				  <option disabled>池上線</option>
				  
					<option >蒲田</option>
					
					<option >蓮沼</option>
					
					<option >池上</option>
					
					<option >千鳥町</option>
					
					<option >久が原</option>
					
					<option >御嶽山</option>
					
					<option >雪が谷大塚</option>
					
					<option >石川台</option>
					
					<option >洗足池</option>
					
					<option >長原</option>
					
					<option >旗の台</option>
					
					<option >荏原中延</option>
					
					<option >戸越銀座</option>
					
					<option >大崎広小路</option>
					
					<option >五反田</option>
					
				
				  <option disabled>多摩川線</option>
				  
					<option >多摩川</option>
					
					<option >沼部</option>
					
					<option >鵜の木</option>
					
					<option >下丸子</option>
					
					<option >武蔵新田</option>
					
					<option >矢口渡</option>
					
					<option >蒲田</option>
					
				
				  <option disabled>大井町線</option>
				  
					<option >二子玉川</option>
					
					<option >上野毛</option>
					
					<option >等々力</option>
					
					<option >尾山台</option>
					
					<option >九品仏</option>
					
					<option >自由が丘</option>
					
					<option >緑が丘</option>
					
					<option >大岡山</option>
					
					<option >北千束</option>
					
					<option >旗の台</option>
					
					<option >荏原町</option>
					
					<option >中延</option>
					
					<option >戸越公園</option>
					
					<option >下神明</option>
					
					<option >大井町</option>
					
				
				  <option disabled>日比谷線</option>
				  
					<option >中目黒</option>
					
					<option >恵比寿</option>
					
					<option >広尾</option>
					
					<option >六本木</option>
					
					<option >神谷町</option>
					
					<option >霞ケ関</option>
					
					<option >日比谷</option>
					
					<option >銀座</option>
					
					<option >東銀座</option>
					
					<option >築地</option>
					
					<option >八丁堀</option>
					
					<option >茅場町</option>
					
					<option >人形町</option>
					
					<option >小伝馬町</option>
					
					<option >秋葉原</option>
					
					<option >仲御徒町</option>
					
					<option >上野</option>
					
					<option >入谷</option>
					
					<option >三ノ輪</option>
					
					<option >南千住</option>
					
					<option >北千住</option>
					
				
			</select>
			<br>
			優先：<select name="priority">
				<option value="fastest">最短経路</option>
				<option value="transfers">乗り換え回数</option>
			</select>
			<br/>
			<input type=submit value="教えて！">
		</form>
		<p>
        <li><a href="http://tokyo.fantasy-transit.appspot.com/map">地図</a></li>
	</body>
</html>
""")

class Route(webapp2.RequestHandler):

	def graph(self):
    graph = {}
    stn = set()
    for line in result:
    	stn.update(set(line['Stations']))
    for station in stn:
	    next_station = {}
        for line in result:
            if station in line['Stations']:
                l = line['Stations']
                name = line['Name']
                idx = l.index(station)
                if idx == 0:
                    next_station[l[1]] = name
                elif idx == len(l)-1:
                    next_station[l[idx-1]] = name
                else:
                    next_station[l[idx-1]] = name
                    next_station[l[idx+1]] = name
        graph[station] = next_station
    return graph

    data = '[{"Name":"山手線","Stations":["品川","大崎","五反田","目黒","恵比寿","渋谷","原宿","代々木","新宿","新大久保","高田馬場","目白","池袋","大塚","巣鴨","駒越","田端駅","西日暮里","日暮里","鶯谷","上野","御徒町","秋葉原","神田","東京","有楽町","新橋","浜松町","田町","品川"]},{"Name":"東横線","Stations":["横浜","反町","東白楽","白楽","妙蓮寺","菊名","大倉山","綱島","日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","自由が丘","都立大学","学芸大学","祐天寺","中目黒","代官山","渋谷"]},{"Name":"目黒線","Stations":["日吉","元住吉","武蔵小杉","新丸子","多摩川","田園調布","奥沢","大岡山","洗足","西小山","武蔵小山","不動前","目黒"]},{"Name":"池上線","Stations":["蒲田","蓮沼","池上","千鳥町","久が原","御嶽山","雪が谷大塚","石川台","洗足池","長原","旗の台","荏原中延","戸越銀座","大崎広小路","五反田"]},{"Name":"多摩川線","Stations":["多摩川","沼部","鵜の木","下丸子","武蔵新田","矢口渡","蒲田"]},{"Name":"大井町線","Stations":["二子玉川","上野毛","等々力","尾山台","九品仏","自由が丘","緑が丘","大岡山","北千束","旗の台","荏原町","中延","戸越公園","下神明","大井町"]},{"Name":"日比谷線","Stations":["中目黒","恵比寿","広尾","六本木","神谷町","霞ケ関","日比谷","銀座","東銀座","築地","八丁堀","茅場町","人形町","小伝馬町","秋葉原","仲御徒町","上野","入谷","三ノ輪","南千住","北千住"]}]'

	result = json.load(data)

	metro = graph(result)

	def fastest(start, end):
		if start == end:
			return [start]
		visited = set()
		queue = [[start]]
		while queue:
			path = queue.pop(0)
			s = path[-1]
			for node, action in metro[s].items():
				if node not in visited:
					visited.add(node)
					path2 = path + [action, node]
					if node == end:
						return path2
					else:
						queue.append(path2)
		return[]
	
	def transfers(start, end):
		if start == end:
			return [start]
		visited = set()
		queue = [[start]]
		while queue:
			path = queue.pop(0)
			s = path[-2]
			line, change = path[-1]
			if s == goal:
				return path
			for node, action in metro[s].items():
				if node not in visited:
				linechange = change
				visited.add(node)
				if  line != action:
					linechange += 1
				path2 = path[:-1] + [action, node, (action, linechange)]
				queue.append(path2)
				queue.sort(key=lambda path:path[-1][-1])
		return []

	def get(self):
		a = self.request.get('from')
		b = self.request.get('to')
		if 'priority'=='fastest':
			c = fastest(a, b)
		elif 'priority'=='transfers':
			c = transfers(a, b)
		res = """<html><body>
				<h2>{}</h2>
				</body></html>""".format(c)
		self.response.headers["Content-Type"] = "text/html"
		self.response.out.write(res)

routes = [('/', MainPage),('/yay', Route)]

app = webapp2.WSGIApplication(routes, debug=True)

# urls = {'joe': 'url1', 'jack': 'url2', 'jane': 'url3'}
# for who in urls.keys():
#     url = urllib.urlopen(urls[who])
#     result = json.loads(url)  # result is now a dict
#     print 'For %s: "networkdiff":' % who, result['getpoolstatus']['data']['networkdiff']