# flake8: noqa
BLOGS = [
    {
        "id": "challenge_blog",
        "title": "Building my Cloud Portfolio",
        "date": "April 30, 2024",
        "topics": "Resume, Portfolio, Azure, CI/CD, Python, HTMX, CSS",
        "content": """
<blockquote>
  <p>"The Cloud Resume Challenge isn't a tutorial or a how-to guide. It's a project spec, and not a very helpful one at that."</p>
  <footer>-Forrest Brazeal</footer>
</blockquote>

<img src="https://cloudresumechallenge.dev/images/multicloud-bundle.gif" style="float: right; width: 35vh" />

<p>The <a class="bloglink" href="#cite_resume_challenge">Cloud Resume Challenge</a> was developed by Forrest Brazeal as a litmus test for prospective cloud developers. It focuses on the skills necessary to be a useful contributor to a company operating on the cloud. Not only is it a test of the dev's ability to build a full-stack app, but can you deploy that app in a scalable way, and can you apply those skills to a prospective employer's problem? The prospective cloud developer is pushed to create a resume that is rendered by a full-stack application running in the cloud.</p>

<p>I began the project with the goal of building a resume, a portfolio, and an in-demand skill set along with a product that I could show on LinkedIn and Github. As soon as I started building the HTML, I knew this project would hold my attention long after I could show employers my resume. And once I had deployed, I was excited to learn everything that Azure could do for me. I suddenly wanted to deploy everything I built. I like programming. I love building useful tools that I can share with others.</p>

<h3>Parts of the Challenge</h3>

<ul>
  <li><b>Front-End:</b> Create the Resume in HTML/CSS</li>
  <li><b>Back-End:</b> Set up source control and visitor counter</li>
  <li><b>Integration:</b> Display the visitor counter on the homepage and increment it on page load</li>
  <li><b>Automation and CI:</b> Deploy the app via the command line and Git repo </li>
  <li><b>Pass the Exam:</b> Take and pass the AZ-900 and write (this) blog!</li>
</ul>

<h3>Azure Fundamentals</h3>

<p>Fresh out of boot camp, I chose to continue my learning and knock out the AZ-900 certification first thing. One week of cramming later, and I was ready to talk all about geo-redundant storage, identity and access management, and ARM templates. My wife learned by radiation more about cloud computing than she ever wanted to know. It was grueling and sometimes snore-inducing, but I managed to nail the exam, so on to the fun stuff!</p>

<h3>Front-end</h3>

<p>The challenge requires the dev to build a static website to host their resume. In the Hack Reactor program, I've written pages in pure HTML and CSS (which Forrest recommends for the challenge), and I've used Django to build the frontend on the backend, then used JS and DOM manipulation, before finally learning React. I knew before starting the challenge that I wasn't going to be satisfied with a simple resume site. I wanted to show off my whole portfolio, and I didn't want to use a generic no-code solution to do so. As long as I'm building this thing anyway, I figured I should make it into something I really wanted to show off.</p>

<p>The front end is a single-page application using HTMX. It took much longer than I expected to code out the frontend and get the CSS just right, but I consider the formatting to be as important as the content for this application. I also took some time away from coding to have an impromptu photo shoot, since I have very few photos of myself alone and without sunglasses.</p>

<img src="img/photoshoot.png" class="blog-img" />

<p>I struggled with attaching the static website endpoint to the domain name system (DNS). I created a canonical name (CNAME) on the domain and checked that the CNAME had been propagated using DNS lookups, but when I accessed the Azure CDN, it would not resolve. I kept getting the error that there was no associated CNAME. I waited hours at a time, thinking it just needed to catch up, but it never resolved. Finally, I found out that Cloudflare provides a proxy which interferes with Azure's ability to resolve the CNAME. After disabling the proxy, the custom endpoint worked just fine. With a working static site, it was time to build the backend.</p>

<h3>Back End and Integration</h3>

<p>Since my webpage operates using GET requests to pull HTML from the server, I already had a backend running in a Python container. I just needed to deploy it. What I didn't know when I built the backend is that I would be using serverless functions to deploy. Serverless functions allow simple websites to operate on the cloud without paying the cost of provisioning a whole virtual machine. It's essentially micro-SaaS (software as a service) architecture, and it allows us to deploy websites virtually for free. </p>

<p>I easily refactored using the Microsoft Learn Quickstart page for Functions, and then deployed using the Azure extension for VSCode. It was quick and easy to set up, after which, I just had to change the URLs in my HTML to use the Azure Function endpoint. With a working full-stack app, it's time to move on to automation.</p>

<h3>Automation and CI</h3>

<p>Setting up the Function App using the VSCode plugin was surprisingly easy, but ARM templates gave me an unreasonable amount of grief. The documentation provides pre-made templates which are very good for getting started when you don't have a plan for your architecture yet. It falls short on explaining how to start from scratch. It's also not easy to find all the options available for a particular attribute. Two major hiccups delayed my project.</p>

<p>First, I easily deployed a storage account using ARM. But when I tried to connect the function app, I got the error "storage account" already exists. This is where I found out that the ARM templates provided by Microsoft sometimes have already made decisions that don't align with my specific use case. I wasn't able to find the setting in functions to use an existing storage account, but I fixed the issue by deploying the function app and storage account on the same template. I realized, if the function app is going to try creating a new one anyway, I can just make sure it creates the storage account I want. </p>

<img src="img/App_diagram.png" class="blog-img" />

<p>The second obstacle came about because the default ARM template for function apps deploys with run-from-package activated. To create the app, I used the ARM template provided by the Create Function App dialog, then I used the Github Action provided in the portal to upload code to the app. The data was successfully uploaded, but the functions were not recognized. A fellow dev from <a class="bloglink" href="#cite_stack_ov_question">Stack Overflow</a> assisted me with troubleshooting, and determined that the Supply Chain Management (SCM) Basic Auth setting was off, and <code>WEBSITE_RUN_FROM_PACKAGE</code> should not be set. This is because the VSCode extension uses remote build, but on consumption plans running Linux, remote builds aren't performed if we use run-from-package. <a class="bloglink" href="#cite_dep_tech">See here for more info.</a></p>

<h3>Reflections</h3>

<p>I spent too long on this project. I walked away from the ARM template problem three times before I turned to Stack Overflow, and once I did the problem was solved within five hours. If I had reached out earlier, I could have spent longer working on other features or learning about remote builds and SCM sites! Meanwhile, on the front end, I spent a long time tweaking small CSS items. I did put the time in there to show myself in the best light. That being said, it doesn't do any good if I'm never actually done and ready to turn on the light.</p>

<p>I haven't even scratched the surface of HTMX. On this page, I change the view using get commands and replacing DOM elements, I update a counter automatically on page load using an hx-post and onLoad trigger, and I update the nav bar using OOB-swaps. I can wait to get into updating browser history and combining HTMX with raw JS scripts. Expanding my frontend skills for this project has been a pleasure.</p>

<img src="img/portfolio_ARM.png" class="blog-img" />

<h3>Conclusion</h3>

<p>I am certainly glad I took on this project. When I started, I looked at deployment as a necessary, but boring, aspect of creating a working project. How wrong I was. I loved diving into each aspect of the project. While I struggled at building ARM templates and got frustrated with connecting the CDN, these were the kind of struggles that made me want to persevere and win, which I ultimately did! </p>

<p>I learned about the structure of cloud platforms and Azure specifically. I learned to navigate Microsoft's arcane documentation sites which made it frustrating to find the information I wanted (although their <a class="bloglink" href="#cite_function_qs">quickstarts</a> and tutorials are pretty nice). And I learned to create Infrastructure as Code solutions. I can't wait to see what I'll start building next.</p>

<p>If you found this post as a fellow up-and-coming dev, I encourage you to host your resume or portfolio on the cloud. It is incredibly fun and educational. If you arrived here as a potential employer, please reach out! I would love to discuss how my skills can help your company achieve its goals.</p>


<h3>References</h3>

<p>
  <a class="bloglink" id="cite_resume_challenge" href="https://cloudresumechallenge.dev/" target="_blank" rel="noopener noreferrer"
  >Cloud Resume Challenge</a>
  <br>
  <a class="bloglink" id="cite_function_qs" href="https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-vs-code-python" target="_blank" rel="noopener noreferrer"
  >Quickstart: Create a function in Azure with Python using Visual Studio Code</a>
  <br>
  <a class="bloglink" id="cite_dep_tech" href="https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies?tabs=windows#key-concepts" target="_blank" rel="noopener noreferrer"
  >Deployment technologies in Azure Functions</a>
  <br>
  <a class="bloglink" id="cite_stack_ov_question" href="https://stackoverflow.com/questions/78281838/when-i-deploy-my-function-app-repository-to-a-new-app-it-doesnt-recognize-any" target="_blank" rel="noopener noreferrer"
  >Question: When I deploy my function app repository to a new app, it doesn't recognize any functions Azure/Python/FunctionApp</a>
</p>

"""
    }
]
