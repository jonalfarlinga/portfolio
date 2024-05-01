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
            hx-swap="outerHtml"
            hx-trigger="showBanner"
            hx-swap-oob="true"
        >About Me</button>
        <button
            class="navlink {'nl-active' if active == 'folio' else ''}"
            id="folio"
            hx-get="{API_HOST}/folio"
            hx-trigger="click"
            hx-target="#content"
            hx-swap="outerHtml"
            hx-trigger="showBanner"
            hx-swap-oob="true"
        >Portfolio</button>
        <button
            class="navlink {'nl-active' if active == 'resume' else ''}"
            id="resume"
            hx-get="{API_HOST}/resume"
            hx-trigger="click"
            hx-target="#content"
            hx-swap="outerHtml"
            hx-trigger="showBanner"
            hx-swap-oob="true"
        >Resume</button>
        <button
            class="navlink {'nl-active' if active == 'vlog' else ''}"
            id="vlog"
            hx-get="{API_HOST}/vlog"
            hx-trigger="click"
            hx-target="#content"
            hx-swap="outerHtml"
            hx-trigger="showBanner"
            hx-swap-oob="true"
        >Video Demos</button>
        <button
            class="navlink {'nl-actve' if active == 'blog' else ''}"
            id="blog"
            hx-get="{API_HOST}/blogpage"
            hx-trigger="click"
            hx-target="#content"
            hx-swap="outerHtml"
            hx-trigger="hideBanner"
            hx-swap-oob="true"
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
      <div class="ps-5 pt-5" id="content">
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
      </div>
    """


def folio_view():
    return (
        navlink("folio") +
        """
        <div class="ps-5 pt-5" id="content">
          <h2>PORTFOLIO</h2>
        </div>
        """ +
        portfolio_cards()
    )


def resume_view():
    return navlink("resume") + """
      <div class="ps-5 pt-5" id="content">
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
            <a
              href="mailto:dennis.bucklin@gmail.com"
              target="_blank"
              rel="noopener noreferrer"
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
      </div>
    """

def vlog_view():
    return navlink("vlog") + """
      <div class="ps-5 pt-5" id="content">
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


def news_view():
    rows = ""
    for blog in BLOGS:
        rows += f"""
          <tr>
            <td>
              <a
                href=''
                hx-get="{API_HOST}/blog?id={blog['id']}"
                hx-target="#blog-content"
              >{blog['title']}</a>
            </td>
            <td>{blog['topics']}</td>
            <td>{blog['date']}</td>
          </tr>
        """
    return navlink("blog") + f"""
      <div class="ps-5 pt-5 blog-content" id="content">
        <h1>Blog List</h1>
        <table>
          <tr>
            <th>Title</th>
            <th>Topics</th>
            <th>Date</th>
          </tr>
          {rows}
        </table>
      </div>
    """

def blog_view(id: str):
    data = {}
    for blog in BLOGS:
        if blog.get('id') == id:
            data = blog
    return f"""
      <div class="ps-5 pt-5 blog-content" id="content">
          <a
            href=''
            hx-get="https://apifunc2kjoo37i24nsw.azurewebsites.net/api/news"
            hx-target="#content"
            hx-swap="outerHtml"
          >Blog List</a>
          <h1>{data.get('title')}</h1>
          <h5 class="mb-5">{data.get('date')} || Topics: {data.get('topics')}</h5>
          <p>{data.get('content')}</p>
      </div>
    """


def blog_page_view():
    return navlink("blog") + """
      <div class="ps-5 pt-5 blog-content" id="content">
"""

def home_page_view(page: str):
    htmx = "Fetching content..."
    match page:
        case 'about':
            htmx = about_view
        case 'folio':
            htmx = folio_view
        case 'vlog':
            htmx = vlog_view
        case 'resume':
            htmx = resume_view
        case _:
            htmx = lambda _: "No content"
    return f"""
    <div class="row p-0 m-0">
      <nav class="d-flex flex-column col-2 p-4">
        <hr />
        <img src="./img/Ulfunnar_Reserve.jpg" class="row logo" alt="logo"/>
        <h6 class="text-warning">
          <div id="page-load" hx-post="https://apifunc2kjoo37i24nsw.azurewebsites.net/api/count" hx-trigger="" hx-target=""></div>
        </h6>
        <hr />
        {navlink(page)}
        <p class="mt-auto text-warning"><a href="https://github.com/jonalfarlinga/portfolio" target="_blank" rel="noopener noreferrer" class="gitlink">Web Portfolio</a> Github repo</p>
      </nav>
      <main class="container-fluid col p-0 m-0">
        <header class="d-flex flex-column justify-content-center m-0 p-5">
          <div class="header-info pt-3" id="info">
            <h1 class="box m-0">Hello, I'm</h1>
            <h1 class="box mb-3">Denny Bucklin</h1>
            <h4 class="box" id="jobtitle">Software Developer</h4>
            <button type="button" class="btn box" data-bs-toggle="modal" data-bs-target="#hireModal">
              Contact Me
            </button>
          </div>
        </header>
        <div class="ps-5 pt-5" id="content">
            {htmx()}
        </div>
      </main>



      <!-- Modal -->
      <div class="modal fade" id="hireModal" tabindex="-1" aria-labelledby="hireModalLabel" aria-hidden="true">
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="hireModalLabel">Contact Info</h1>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <h3>Phone</h3>
              <ul>
                <li>
                  <p><b>Phone:</b>
                    +1-562-619-6459
                  </p>
                </li>
              </ul>
              <h3>Email</h3>
              <ul>
                <li>
                  <p><b>Email:</b>
                    <a href="mailto:dennis.bucklin@gmail.com">dennis.bucklin@gmail.com</a>
                  </p>
                </li>
              </ul>
              <h3>Sites</h3>
              <ul>
                <li>
                  <a
                    target="_blank"
                    rel="noopener noreferrer"
                    href="http://www.linkedin.com/in/dennis-bucklin"
                  >LinkedIn</a>
                </li>
                <li>
                  <a
                    target="_blank"
                    rel="noopener noreferrer"
                    href="https://github.com/jonalfarlinga"
                  >Github for personal projects</a>
                </li>
                <li>
                  <a
                    target="_blank"
                    rel="noopener noreferrer"
                    href="https://gitlab.com/dennis.bucklin"
                  >Gitlab for education projects</a>
                </li>
                <li>
                  <a
                    target="_blank"
                    rel="noopener noreferrer"
                    href="https://public.tableau.com/app/profile/dennis.bucklin/vizzes"
                  >Tableau - Data Visualizations</a>
                </li>
                <li>
                  <a
                    target="_blank"
                    rel="noopener noreferrer"
                    href="https://www.kaggle.com/dennisbucklin"
                  >Kaggle - Data science and machine learning projects</a>
                </li>
              </ul>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn" data-bs-dismiss="modal">Close</button>
            </div>
          </div>
        </div>
      </div>
      <script src="https://unpkg.com/htmx.org@1.9.10/dist/htmx.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    </div>
"""
