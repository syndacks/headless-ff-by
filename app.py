# inspired by https://www.lambdatest.com/blog/adding-firefox-extensions-with-selenium-in-python/

from datetime import datetime
from flask import Flask, render_template, request, flash
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time


app = Flask(__name__)
app.config['SECRET_KEY'] = '91bc94c544e2628957afec01ecfe6fecae1a60ed454cece0'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/bypass/', methods=('GET', 'POST'))
def bypass():
        if request.method == 'POST':
            article_url = request.form['article_url']

            if not article_url:
                flash('article url is required!')
            else:
                try:
                    bypass_paywall_xpi_path = "/Users/dacksmilliken/Downloads/bypass-paywalls-firefox.xpi"
                    ublock_origin_xpi_path = "/Users/dacksmilliken/Downloads/ublock_origin-1.40.8-an+fx.xpi"

                    firefox_options = Options()
                    firefox_options.add_argument("--headless")
                    driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=firefox_options)

                    driver.install_addon(bypass_paywall_xpi_path, temporary=True)
                    driver.install_addon(ublock_origin_xpi_path, temporary=True)
                    time.sleep(1)

                    driver.get(article_url)
                    time.sleep(1)

                    HELLO_HTML="""
                        <html><body>
                            <h1>Hello, syndacks!</h1>
                            {0}
                        </body></html>
                    """
                    return HELLO_HTML.format(driver.page_source)
                except Exception as E:
                    print(E)
                finally:
                    driver.quit()


        return render_template('bypass.html')


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", debug=True)