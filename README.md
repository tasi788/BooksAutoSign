# BooksAutoSign

博客來里程自動簽到。

我很懶沒有圖，謝謝。

# 安裝方法
1. 請先給我星星，接著點 `Fork` \
![1](https://user-images.githubusercontent.com/11913223/142626560-ea53d1fc-181a-43e1-b4c4-c003fcc50f90.png)

2. 安裝這[個東西](https://chrome.google.com/webstore/detail/copy-cookies/jcbpglbplpblnagieibnemmkiamekcdg)支援 Chrome, Edge

3. 登入[博客來里程](https://myaccount.books.com.tw/myaccount/myaccount/memberReadMileage)

4. 在博客來里程頁面點一下剛剛安裝的擴充套件，會替你複製餅乾到剪貼簿，將複製的東西先貼到一個安全的地方 \
![2](https://user-images.githubusercontent.com/11913223/142627783-162894c8-270e-45a2-807b-993fefa336a6.png)

5. 新增一個 [Personal Access Token](https://github.com/settings/tokens/new)
最後點擊綠色的 `Generate token` \
![3](https://user-images.githubusercontent.com/11913223/142715936-b32bc0fa-30e6-4d8d-84d8-7f340d49842b.png)

6. 複製顯示出來的 `Personal Access Token` 該 token 只會顯示一次，離開頁面就不會再顯示了。 \
將複製出來的 token 新增到 Secret 內，名稱輸入 `GH_TOKEN` \
![4](https://user-images.githubusercontent.com/11913223/142715949-dafb693c-0d13-48a5-9793-d28a679ff7ff.png)

7. 回到 repo 之後點一下 `Setting` \
![5](https://user-images.githubusercontent.com/11913223/142626734-a402341e-5c5e-4a7b-8e48-4358246daa3e.png)

8. 點左邊的 `Secret` 著右上角的 `New repository secret` \
![6](https://user-images.githubusercontent.com/11913223/142627052-96f71ad3-19c2-40df-a189-e1e75b8665bb.png)

9. 分別新增 `BOOKS_COOKIE` 貼上剛剛擴充套件複製的餅乾。 \
想要啟用 telegram 通知則新增 `BOT_TOKEN`、`CHAT_ID`，若不知道 telegram 通知參數請[參閱](https://github.com/tasi788/PTTAutoSign#faq)。

10. 最後回到 `repo` 點一下 `action` 記得啟用 `workflows` 喔 \
![7](https://user-images.githubusercontent.com/11913223/142715969-bbe0efdf-a4e6-4842-af5a-9371fe84ba86.jpeg)

11. 自動同步更新原始碼，請點[這裡](https://github.com/apps/pull)，並點一下綠色的 Install

12. 點 `Only select repositories` 選擇剛剛 fork 走的 repo。

13. Enjoy ✨
