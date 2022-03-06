<h1>
<p align=center>
<img src="./unsplash-welcome.jpg">
</p>
</h1>

<h2><b> Bot Usage</b> </h2>

<table>
    <tr>
        <th>Command</th>
        <th>Description</th>
    </tr>
    </tr>
        <td><code>/start</code></td>
        <td>Start the bot.</td>
    </tr>
    <tr>
        <td><code>/photo | /image | /search     < Query ></code></td>
        <td>Search photos on Unsplash.</td>
    </tr>
    <tr>
        <td><code>/random | /rand < Count ></code></td>
        <td>Get random photos from Unsplash <i>Specifying the <code>Count</code> is not important.<i></td>
    </tr>
</table>

<h2><b>Run Locally</b></h2>

* Clone the Repo.
```sh
git clone https://github.com/bibee-emio/Unsplash-bot
```
* Change the Directory.
```sh
cd Unsplash-bot
```
* Install the requirements.
```sh
pip3 install -r requirements.txt
```
* Edit the `config.py` with your own values.
* Run the bot.
```sh
python3 bot.py
```

<h2><b>Deploy to Heroku</b></h2>

* Click on the following button.

<a href="https://heroku.com/deploy?template=https://github.com/bibee-emio/Unsplash-bot">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy"
  style="padding:15px">
</a>

<h2><b>Special Credits</b></h2>

- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [Unsplash](https://unsplash.com/)
