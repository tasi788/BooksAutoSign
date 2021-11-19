# BooksAutoSign

博客來里程自動簽到。

我很懶沒有圖，謝謝。

# 安裝方法
1. 請先給我星星，接著點 `Fork` \
![1](https://user-images.githubusercontent.com/11913223/142626560-ea53d1fc-181a-43e1-b4c4-c003fcc50f90.png)

2. 安裝這[個東西](https://chrome.google.com/webstore/detail/copy-cookies/jcbpglbplpblnagieibnemmkiamekcdg)支援 Chrome, Edge

3. 登入[博客來里程](https://myaccount.books.com.tw/myaccount/myaccount/memberReadMileage)

4. 在博客來里程頁面點一下剛剛安裝的擴充套件 \
![2](https://user-images.githubusercontent.com/11913223/142627783-162894c8-270e-45a2-807b-993fefa336a6.png)

5. 對網頁空白處點右鍵，選擇「元素」 \
![3](https://user-images.githubusercontent.com/11913223/142629697-bd36b307-1e94-436a-9a3e-6d0a02bb525b.png)

6. 在彈出的視窗選取 `console`，並輸入 `cookie=` 接著 `ctrl+v` 貼上剛剛擴充套件替你複製的東西。 \
![4](https://user-images.githubusercontent.com/11913223/142630526-93e0a59b-3098-4748-b7b0-7cbaa149b656.png)

7. 並將 [index.js](https://github.com/tasi788/BooksAutoSign/blob/main/index.js) 裡的東西複製貼上並 `Enter` 執行，將輸出的東西複製起來。

9. 回到 repo 之後點一下 `Setting` \
![5](https://user-images.githubusercontent.com/11913223/142626734-a402341e-5c5e-4a7b-8e48-4358246daa3e.png)


3. 點左邊的 `Secret` 著右上角的 `New repository secret` \
![3](https://user-images.githubusercontent.com/11913223/142627052-96f71ad3-19c2-40df-a189-e1e75b8665bb.png)





4. 分別新增 `BAHA_UID`、`BAHA_PASSWD` 內容分入帳號跟密碼。 \
如果有設定 2FA 則記得新增 `BAHA_2FA` 填入 2FA 的密鑰。  \
想要啟用 telegram 通知則新增 `BOT_TOKEN`、`CHAT_ID`，若不知道 telegram 通知參數請[參閱](https://github.com/tasi788/PTTAutoSign#faq)。 \
![4.png](./pic/4.png)
