# https://github.com/pywinauto/pywinauto

from pywinauto import Application, mouse

mouse_position = mouse.get_position()

app = Application().connect(handle=mouse.get_foreground_window())

window_title = app.top_window().window_text()

mouse.click(button='left', coords=mouse_position)

print("current active window:", window_title)

「～てあります」和「～ておきます」雖然都涉及動作的結果，但它們的重點不同：「～てあります」強調狀態，而「～ておきます」強調目的性和準備。

**1. 「～てあります」——**強調狀態

**「～てある」**表示某個動作已經被完成，而且這個狀態還在持續。這通常是指某人（可能不是說話者）做了某個動作，導致現在的狀態。

句型結構

	•	他動詞（て形）+ ある
	•	（要用他動詞，不能用自動詞）

用法

	1.	強調動作的結果還在
	•	窓が開けてあります。（窗戶開著。）（= 有人開了窗，現在窗戶是開著的狀態。）
	•	会場にいすが並べてあります。（會場的椅子被擺好了。）
→ 重點在於「現在是這樣的狀態」，而不是誰做的。
	2.	表示事前準備完成（結果持續）
	•	テストの問題がもう作ってあります。（考試題目已經做好了。）
→ 重點在於「題目已經被做好」，現在可以使用。

**2. 「～ておきます」——**強調目的和準備

「～ておく」表示為了某個目的，事先完成一個動作，或者讓某個動作維持一段時間。

句型結構

	•	動詞（て形）+ おく

用法

	1.	事先準備
	•	明日の会議の資料をコピーしておきます。（先把明天的會議資料影印好。）
→ 重點是「為了明天的會議，現在先準備好」。
	2.	為了某個狀況，暫時保持現狀
	•	このままにしておいてください。（請先保持這樣。）
	•	ドアを開けておきます。（先把門開著。）
→ 強調「故意不關」，不是單純的「門開著」。
	3.	動作之後不用再管
	•	質問があったら、メモしておいてください。（有問題的話請記下來。）
→ 記下來，之後可以參考或再問。

3. 「～てあります」 vs. 「～ておきます」的比較

	～てあります（狀態）	～ておきます（準備）
句型	他動詞 + てある	動詞 + ておく（自他動詞皆可）
重點	強調結果的持續狀態	強調事前準備或有目的的動作
誰做的	通常不強調	說話者或已知的人做的
例句 1	エアコンがつけてあります。（冷氣已經開著。）	暑いので、エアコンをつけておきます。（因為很熱，先開好冷氣。）
例句 2	料理が作ってあります。（菜已經做好了。）	今夜のために料理を作っておきます。（為了今晚，先做好菜。）

4. 例句對比

	1.	書類
	•	書類が机の上に置いてあります。（文件已經放在桌上了。）→ 重點是現在「文件在桌上」的狀態。
	•	会議のために、書類を机の上に置いておきます。（為了開會，先把文件放在桌上。）→ 重點是「事先準備」的目的。
	2.	電視
	•	テレビがつけてあります。（電視是開著的狀態。）→ 誰開的不重要，現在就是這樣。
	•	ニュースを見るために、テレビをつけておきます。（為了看新聞，先把電視打開。）→ 強調開電視的目的。

5. まとめ（總結）

	•	「～てあります」：動作已完成，現在的狀態是這樣。
	•	「～ておきます」：為了某個目的，先做某件事。

這兩者的區別有時很細微，但如果你抓住「狀態 vs. 目的」的概念，就能比較準確地使用了！

「～しませんでした」和「～しましたか」的區別主要在於否定與疑問，它們的基本結構如下：

句型	否定過去	疑問句
原形	～しませんでした（沒做…）	～しましたか（做了嗎？）
語氣	確定事實，表示過去未發生	詢問對方是否做過某件事
例句	昨日、運動しませんでした。（昨天沒運動。）	昨日、運動しましたか。（昨天有運動嗎？）

1. 「～しませんでした」—— 否定過去

「～しませんでした」是「～する」的過去否定形，表示「沒有做某事」。

句型結構

	•	動詞（ます形）+ しませんでした（= 過去否定）
	•	例：勉強します → 勉強しませんでした（沒學習）
	•	例：食べます → 食べませんでした（沒吃）

用法

	1.	表達某件事在過去沒有發生
	•	昨日、映画を見ませんでした。（昨天沒看電影。）
	•	朝ごはんを食べませんでした。（沒吃早餐。）
	2.	用於委婉拒絕
	•	その本は読みませんでした。（那本書我沒看過。）
→ 比「読まなかった」更正式或有禮貌。

2. 「～しましたか」—— 疑問句

「～しましたか」是「～する」的過去疑問形，用來詢問某件事是否發生過。

句型結構

	•	動詞（ます形）+ しましたか（= 過去疑問）
	•	例：勉強します → 勉強しましたか（有學習嗎？）
	•	例：食べます → 食べましたか（有吃嗎？）

用法

	1.	詢問對方是否做過某事
	•	昨日、映画を見ましたか？（昨天有看電影嗎？）
	•	朝ごはんを食べましたか？（有吃早餐嗎？）
	2.	確認某件事是否發生
	•	宿題はもう終わりましたか？（作業已經做完了嗎？）
	•	仕事は終わりましたか？（工作結束了嗎？）

3. 例句對比

日文句子	中文意思	否定 / 疑問
昨日、運動しましたか？	昨天有運動嗎？	疑問句，詢問對方
昨日、運動しませんでした。	昨天沒運動。	否定句，陳述過去沒有做
晩ご飯を食べましたか？	晚餐有吃嗎？	詢問對方
晩ご飯を食べませんでした。	沒吃晚餐。	陳述事實

4. 總結

句型	意思	語氣
～しませんでした	沒有做某事	陳述過去未發生
～しましたか？	做了某事嗎？	詢問對方是否做過

這兩者的主要差異是否定 vs. 疑問，一個是陳述過去沒有發生，一個是詢問是否發生！
「行く（いく）」和「来る（くる）」都是表示移動的動詞，但它們的主要差異在於移動的方向性和視角。

1. 主要區別

動詞	中文意思	方向	參考點
行く（いく）	去	從說話者所在的地方移動到別的地方	以說話者為基準，向外移動
来る（くる）	來	從別的地方移動到說話者所在的地方	以說話者為基準，向內移動

簡單例子

	1.	学校へ行く。（去學校。）→ 移動到學校（別的地方）
	2.	学校へ来る。（來學校。）→ 移動到學校（說話者在學校或與對方約定學校作為參考點）

2. 行く vs. 来る 的使用場景

（1）根據說話者的視角選擇

A：你在家裡，朋友在外面

	•	朋友：「今から君の家に 行くよ！」（現在要去你家！）
→ 朋友從外面移動到你的家，對他來說是「去」。
	•	你：「じゃあ、うちに 来てね！」（那就來我家吧！）
→ 你的家是參考點，朋友移動到你的位置，對你來說是「來」。

（2）約定時的用法

你和朋友相約在咖啡店見面

	•	朋友已經在咖啡店，你說：「今からカフェに行くよ！」
→ 你從家裡移動到咖啡店，對你來說是「去」。
	•	你已經在咖啡店，朋友說：「今からカフェに来るよ！」
→ 朋友從別的地方移動到你所在的咖啡店，對他來說是「來」。

（3）邀請別人時

	1.	遊びに行く（去玩） vs. 遊びに来る（來玩）
	•	友達の家に遊びに行く。（去朋友家玩。）
→ 以自己為基準，從自己所在的地方移動到朋友家。
	•	友達が家に遊びに来る。（朋友來我家玩。）
→ 朋友從別的地方移動到自己的家。
	2.	「來不來？」的不同問法
	•	週末、映画を見に行かない？（週末要不要去看電影？）
→ 以雙方為基準，指雙方要一起去別的地方。
	•	週末、うちに来ない？（週末要不要來我家？）
→ 以說話者為基準，邀請對方移動到說話者的家。

（4）表達時間的變化

「来る」還能用來表達時間的變化，而「行く」不常這樣用：

	•	春が来る。（春天要來了。）→ 從現在移動到未來，以現在為參考點。
	•	時代が変わっていく。（時代漸漸改變。）→ 以現在為基準，向未來發展。

3. 其他特殊用法

（1）慣用表達

有些固定用法不能直接翻譯成「去」或「來」，例如：

	•	気がつく vs. 気が来る
	•	気がつく（注意到）
	•	気が来る（精神失常，瘋掉）

（2）補助動詞的用法

「行く」和「来る」也常用作補助動詞：

	•	～ていく：表示動作向遠方發展或持續進行。
	•	暑くなっていく。（會越來越熱。）
	•	日本語を勉強していく。（會持續學習日語。）
	•	～てくる：表示動作接近或已經發生。
	•	雨が降ってきた。（開始下雨了。）
	•	彼が走ってきた。（他跑過來了。）

4. 總結

用法	行く（いく）	来る（くる）
基本意思	去	來
方向	離開說話者，移動到別的地方	接近說話者，移動到說話者所在的地方
例句	日本へ行く（去日本）	日本へ来る（來日本）
邀請	遊びに行かない？（要不要去玩？）	うちに来ない？（要不要來我家？）
時間表達	ー	春が来る（春天來了）
補助動詞	～ていく（持續、向遠發展）	～てくる（開始、朝自己靠近）

這兩個詞雖然看似簡單，但在不同語境下有細微的區別，需要依據視角來選擇正確的用法。
