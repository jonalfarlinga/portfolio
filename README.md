# My Portfolio
### The Cloud Resume Challenge

## Description
This portfolio contains the index and the backend dev environment for my cloud resume.  The live portfolio/resume can be found at [portfolio.denny-bucklin.net](portolio.denny-bucklin.net).

## Tech Stack
- The main page is built with **HTML** and **CSS**, utilizing Bootstrap for styling.
- I use **HTMX** and a **Python** backend to serve the separate page views.
- The backend interacts with an **Azure Table** in blob storage to get and update a count of page loads.
- The `index.html` is a static web page served from an **Azure Storage** account, using a custom endpoint and custom domain name to connect.
- The backend API is served from an **Azure Functions App**

## Installation
If you want to recreate the dev environment, it's simple. Begin by downloading this code-base.

1. Navigate to the `/dev/python` directory in the terminal and install a Python Virtual Environment: `python -m venv .venv`
2. Activate the new virtual environment (this step will differ based on your OS)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the Uvicorn server: `uvicorn main:app --host 0.0.0.0 --reload`
5. Copy the absolute path to `/public/index_dev.html` and paste it in your browser.

You should now see the basic page, with the About page fetched on page load.

## The Experience
- I decided to learn a new technology with this project: **HTMX**. It was a lot of fun, even though I've only scratched the surface. My first real hurdle was was trying to change the `#content` div and the `nav` items with one request, but once I discovered the OOB swap, it was a breeze.

- Using a backend to serve the **HTMX** fetches means that I couldn't follow the challenge exactly. I had to have the API up and runnning in order to have the website running, even without a site-visit counter or database to contact.

- I struggled to set up a `CNAME` for my custom domain. I was able to add the record on Cloudflare all right, but it would never show up on nslookup.io. Finally, after much fiddling, I found out that the Cloudflare proxy was preventing Azure from reaching the `CNAME` record. After correcting this, I rapidly fixed the issues and brought the site up live through my custom server.

- There are a number of environment variables in the Github Actions pipeline. I tried several ways to add a necessary key to the pipeline, and kept having issues, until I learned that Github Actions variables are not accessible by my functions. I looked up where to add variables in Azure Functions, and found out that the variable I was triyng to add already exists in the Functions environment.

- I have to be careful about the prodducts I use from Azure. The wrong subscription can add up quickly.

## Authors and acknowledgment
This project is written by and for Denny Bucklin.

The project follows the path laid out in **The Cloud Resume Challenge Guidebook** by Forest Brazeal.

## Dev Roadmap
- I would like to add Github Actions to keep `index.html` and `index.css` automatically updated on Azure.

- I want to add a testimonials page

- I plan to add a tab with my experiences building this project

- Updates for project tags
  - [ ] Technical Link
  - [ ] Website Link
  - [ ] Description of Project
  - [ ] Tech Stack
  - [ ] Image File Name
  - [ ] Project Demo
