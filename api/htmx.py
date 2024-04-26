from api.projects import PROJECTS
from api.blogs import BLOGS
API_HOST = "https://apifunc2kjoo37i24nsw.azurewebsites.net/api"
# flake8: noqa Linting disabled to allow for long lines in HTML

def navlink(active: str):
    return f"""
        <button
            class="navlink {'nl-active' if active == 'about' else ''}"
            id="about"
            hx-get="{API_HOST}/about"
            hx-trigger="click"
            hx-target="#content"
            hx-swap-oob="true"
        >About Me</button>
        <button
            class="navlink {'nl-active' if active == 'folio' else ''}"
            id="folio"
            hx-get="{API_HOST}/folio"
            hx-trigger="click"
            hx-target="#content"
            hx-swap-oob="true"
        >Portfolio</button>
        <button
            class="navlink {'nl-active' if active == 'resume' else ''}"
            id="resume"
            hx-get="{API_HOST}/resume"
            hx-trigger="click"
            hx-target="#content"
            hx-swap-oob="true"
        >Resume</button>
        <button
            class="navlink {'nl-active' if active == 'vlog' else ''}"
            id="vlog"
            hx-get="{API_HOST}/vlog"
            hx-trigger="click"
            hx-target="#content"
            hx-swap-oob="true"
        >Video Demos</button>
        <button
            class="navlink"
            id="blog"
            hx-get="https://portfolio.denny-bucklin.net/blog"
            hx-trigger="click"
            hx-target="html"
            hx-swap="outerHTML"
        >Blog</button>
    """


def portfolio_cards():
    html = '<div class="row row-cols-3">'
    for project in PROJECTS:
        html += f"""
            <div class="card col" style="width: 18rem;">
              <img
                src={project.get('src')}
                class="card-img-top"
                alt={project.get('alt')} />
              <div class="card-body">
                <h5 class="card-title">{project.get('name')}</h5>
                <p class="card-text">{project.get('description')}</p>
                <p class="card-text">{project.get('stack')}</p>
              </div>
              <button
                type="button" class="btn btn-primary"
                data-bs-toggle="modal"
                data-bs-target="#{project.get('id')}Modal"
              >More</button>
            </div>
            <!-- Modal -->
            <div
              class="modal fade" id="{project.get('id')}Modal"
              tabindex="-1"
              aria-labelledby="{project.get('id')}ModalLabel"
              aria-hidden="true"
            >
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1
                      class="modal-title fs-5"
                      id="{project.get('id')}ModalLabel"
                    >{project.get('name')} Project</h1>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                  </div>
                  <div class="modal-body">
                    {project.get('body')}
                  </div>
                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn"
                      data-bs-dismiss="modal"
                    >Close</button>
                  </div>
                </div>
              </div>
            </div>
        """
    html += "</div>"

    return html


def about_view():
    return navlink("about") + """
        <h2>ABOUT ME</h2>
          <div>
          <div id="headshot">
            <img src="./img/square_headshot.png" />
          </div>
          <p><b>Name:</b> Denny Bucklin</p>
          <p><b>Location:</b> San Marcos, TX</p>
          <p><b>Email:</b> <a href="mailto:dennis.bucklin@gmail.com"> dennis.bucklin@gmail.com</a></p>
          <p class="pb-3">
            I aspire to design impactful systems that aid people regardless of scale, and I aim to be a reliable support figure providing assistance to my peers when needed. In essence, I am driven by a relentless pursuit of knowledge, blending technical expertise with a collaborative spirit and a passion for crafting solutions that truly make a difference.
          </p>
          <div class="text-center row">
            <p class="col text-warning">Team Leader</p>
            <p class="col text-warning">Process Optimization</p>
            <p class="col text-warning">Analytical Prowess</p>
            <p class="col text-warning">Passionate Developer</p>
          </div>
        </div>
    """


def folio_view():
    return (
        navlink("folio") +
        "<h2>PORTFOLIO</h2>" +
        portfolio_cards()
    )


def resume_view():
    return navlink("resume") + """
        <div>
          <h2>RESUME</h2>
          <div id="pdf">
            <a
              href="https://portfolio.denny-bucklin.net/docs/Resume.pdf"
              target="_blank"
              rel="noopener noreferrer"
              style="padding-right: 0;"
            >PDF Resume</a>
          </div>
          <style>#pdf { text-align: right; display: block; margin-right: 2em }</style>
          <h3>Full Stack Developer</h3>
          <h6>Phone: (562) 619-6459 |
            <a href="mailto:dennis.bucklin@gmail.com"
          >dennis.bucklin@gmail.com</a> | San Marcos, TX </h6>
          <hr/>
          <h4>Technical Skills</h4>
          <p>
            <b>Programming Languages</b> | JavaScript ES6+, Java 21, SQL, HTML5, CSS, Python 3, R 4.3.2, Mongosh
            <b>Front-End</b> | HTMX, React 18, Next.js, DOM manipulation
            <b>Back-End</b> | Node, Django, FastAPI, Flask
            <b>Other</b> | Git, CI/CD, Docker, Azure, Deployment, Authorization, Tableau
          </p>
          <hr/>
          <h4>Revelant Projects</h4>
          <p>
            <b>Backend Lead | Birddex | React, FastAPI, Python, PostgreSQL</b>
            <ul>
              <li>Designed unit tests and debugged errors using Python unittest to ensure performant and reliable software</li>
              <li>Optimized queries using FastAPI and PostgresQL to serve data to the front end app</li>
              <li>Built a frontend using React to present a single-page application and Redux and RTK Query to minimize component coupling</li>
              <li>Developed using Docker collaboratively with a group, focusing on inclusivity and Agile methodologies</li>
              <li>Deployed using a cloud provider on the backend and Gitlab Pages for the frontend</li>
              <li>Live Project: <a href=https://birddex-canarydevs-7c43724f43a204a4ae45736f97fbd05a88591d9dbc16.gitlab.io/>https://canarydevs.gitlab.io/birddex/</a></li>
            </ul>
          </p>
          <p>
            <b>Full Stack Developer | Calends-Online |  React, Python, FastAPI, Azure</b>
            <ul>
              <li>Automated the data entry process using Python requests library for web scraping & Beautiful Soup library for handling HTML inputs saving user time and effort when generating a syllabus</li>
              <li>Personalized solutions based on feedback gathered through customer interviews to best address & exceed user needs</li>
              <li>Employed Azure Web Apps to host the live application</li>
              <li>Live Project: <a href=https://calends.proficientdr.com>https://calends.proficientdr.com</a></li>
            </ul>
          </p>
          <p>
            <b>Service Engineer | Dealer's Choice | React, Python, Django</b>
            <ul>
              <li>Constructed microservices in Docker with a Django backend</li>
              <li>Created stateful components to handle Autos, Errors, Sales, etc. with React</li>
              <li>Implemented filtering of Services by VIN to provide users with important information easily and quickly</li>
            </ul>
          </p>
          <p>
            <b>Data Analyst | Health Outcomes for Horses | Python</b>
            <ul>
              <li>Processed and cleaned data using Python for data mining and manipulation to increase accuracy and performance of machine learning models</li>
              <li>Utilized Python libraries including Numpy, Pandas, & Statistics, along with machine learning models such as LightGBM, XGBoost, Sklearn to identify key trends, patterns, & predict individual outcomes on Kaggle</li>
              <li>Notebook : <a href=https://www.kaggle.com/code/dennisbucklin/health-outcomes-for-horses-competition>https://www.kaggle.com/code/dennisbucklin/health-outcomes-for-horses-competition</a></li>
            </ul>
          </p>
          <hr/>
          <h4>Education</h4>
          <p>
            <b>Software Engineering with Javascript and Python | Hack Reactor</b>
            <ul>
              <li>Built running applications based on software requirements</li>
              <li>Learned and applied Domain Driven Design</li>
              <li>Deployed near-real-time applications using SQL and FastAPI</li>
            </ul>
          </p>
          <p>
            <b>Azure Fundamentals | Microsoft</b>
            <ul>
              <li>Learned the basics of cloud computing and Azure services</li>
              <li>Understood the value of cloud computing and how it can help businesses</li>
            </ul>
          </p>
          <p>
            <b>Google Data Analytics | Coursera Certificate</b>
            <ul>
              <li>Practiced data analysis tasks (data wrangling, pivot tables, data mining, and charts) using Jupyter, Excel, and R.</li>
            </ul>
          </p>
          <p>
            <b>Economics, B.A. | University of Southern Mississippi</b>
            <ul>
              <li>Research Methods, Advanced Algebra, Capstone Research Project using Multiple Regression</li>
            </ul>
          </p>
          <hr/>
          <h4>Professional Experience</h4>
          <p>
            <b>AI Trainer | Freelance</b>
            <ul>
              <li>Analyzed language model outputs to improve the efficacy of end-user interactions with AI</li>
              <li>Developed and refined coding challenges for AI chatbots in Python and Java</li>
              <li>Authored high-quality solutions and explanations for complex coding problems, ensuring clear understanding and application of programming concepts in AI model development</li>
            </ul>
          </p>
          <p>
            <b>Field Engineer | Insituform Technologies</b>
            <ul>
              <li>Enhanced operational efficiency & quality by 15 percent using statistical analysis to develop SOPs, resulting in a 15 percent reduction in errors</li>
              <li>Oversaw production and delivery operations for manufacturing plant earning $1 mil monthly revenue</li>
              <li>Preserved operational readiness and designed and implemented training for 15 manufacturing employees</li>
            </ul>
          </p>
          <p>
            <b>Petty Officer | United States Coast Guard</b>
            <ul>
              <li>Maintained physical plant of 4 boats, 2 cars, 4 small engines, and 1 diesel generator to achieve 100% operational readiness</li>
              <li>Trained 14 peers and subordinates to maintain machinery, operate radios, etc.</li>
              <li>Ensured public & commercial boating safety & security by standing radio guard, utilizing VHS radio & multi-line phone</li>
            </ul>
          </p>
        </div>
    """

def vlog_view():
    return navlink("vlog") + """
      <div>
        <h2 class="mb-3">DEMOS</h2>
        <div>
          <h4>LeetCode75</h4>
          <a
            href="https://www.youtube.com/playlist?list=PLg92KPokRp2zgOolEORM5m9TcvVrUjo1G"
            target="_blank"
            rel="noopener noreferrer"
          >Youtube Playlist</a>
          <h4>Birddex Video Demo</h4>
          <a
            href="https://youtu.be/xJsiBTLnWy4"
            target="_blank"
            rel="noopener noreferrer"
          >Video Demo</a>
        </div>
      </div>
    """


def blog_view():
    rows = ""
    for blog in BLOGS:
        rows += f"""
          <tr>
            <td><a href="{blog['link']}">{blog['title']}</a></td>
            <td>{blog['topics']}</td>
            <td>{blog['date']}</td>
          </tr>
        """
    return """
        <h1>Blog List</h1>

        <table>
          <tr>
            <th>Title</th>
            <th>Topics</th>
            <th>Topics</th>
          </tr>
          <tr>
            <td><a href="">Building the Cloud Resume</a></td>
          </tr>
        </table>
    """
