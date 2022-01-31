# inspired by https://www.lambdatest.com/blog/adding-firefox-extensions-with-selenium-in-python/

from datetime import datetime
from flask import Flask, render_template, request, flash
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import os
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = '91bc94c544e2628957afec01ecfe6fecae1a60ed454cece0'
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}]

def which(pgm):
    path=os.getenv('PATH')
    for p in path.split(os.path.pathsep):
        p=os.path.join(p,pgm)
        if os.path.exists(p) and os.access(p,os.X_OK):
            return p

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
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    bypass_paywall_xpi_path = "{0}/xpis/bypass-paywalls-firefox.xpi".format(dir_path)
                    print("bypass_paywall_xpi_path: ", bypass_paywall_xpi_path)

                    ublock_origin_xpi_path = "{0}/xpis/ublock_origin-1.40.8-an+fx.xpi".format(dir_path)
                    print("ublock_origin_xpi_path: ", ublock_origin_xpi_path)



                    firefox_options = Options()
                    firefox_options.add_argument("--headless")
                    print("1")
                    
                    os.which=which
                    geckodriver_path = which('geckodriver')
                    print("geckodriver_path: ", geckodriver_path)

                    # driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=firefox_options)
                    driver = webdriver.Firefox(executable_path=geckodriver_path, options=firefox_options)

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
