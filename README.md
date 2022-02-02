# headless-ff-by
Hey, this little project is the function of me switching from Android to iOS. One of the things that I miss most about Android is the ability to load browser extensions.

Here I create a simple Flask server that takes a URL, and then loads that URL in a Firefox (Geckodriver) headless environment with a few browser extensions installed to do things I want with the URL I give it. Then, Selenium grabs the source, and returns it back to the Flask server.

This all works fine but I want this to run on my old Android as the server. I'm having trouble installing Docker on my Android (which is running Termux).


Original inspiration
https://www.lambdatest.com/blog/adding-firefox-extensions-with-selenium-in-python/

Intalling Docker on Termux
https://gist.github.com/oofnikj/e79aef095cd08756f7f26ed244355d62

Installing Docker on a Rooted Device
https://gist.github.com/FreddieOliveira/efe850df7ff3951cb62d74bd770dce27
