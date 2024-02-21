from projects import PROJECTS
API_HOST = "https://bucklin-portfolio-fetch.azurewebsites.net/api"
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
            A full stack software developer with a proven track record in process optimization and analytical prowess. Expert in leading teams, implementing efficient protocols, and ensuring seamless operations. Adept at leveraging technology for impactful results.
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
          <a id="pdf" href="https://drive.google.com/file/d/1AL8CKGTNFag81yr3OWzCZue2ECYXZQex/view?usp=sharing">PDF Resume</a>
          <style>#pdf { text-align: right; width: 100%; display: block }</style>
          <h3>Full Stack Developer</h3>
          <h6>Phone: (562) 619-6459 |
            <a href="mailto:dennis.bucklin@gmail.com"
          >dennis.bucklin@gmail.com</a> | San Marcos, TX </h6>
          <hr/>
          <h4>Technical Skills</h4>
          <p>
            <b>Programming Languages</b> | JavaScript ES6+, Java 21, SQL, HTML5, CSS, Python 3, R 4.3.2
            <b>Front-End</b> | React 18, Next.js, DOM manipulation
            <b>Back-End Frameworks</b> | Node, Django, FastAPI
            <b>Other</b> | Git, CI/CD, Docker, Deployment, Authorization, Tableau
          </p>
          <hr/>
          <h4>Revelant Projects</h4>
          <p>
            <b>Backend Lead | Birddex | React, FastAPI, Python, PostgreSQL</b>
            <ul>
              <li>Designed and implemented a card list display with mutable-length rows and interspersed with accordion lists</li>
              <li>Built a backend including authorization using JWT and RESTful API and a frontend using React Redux and RTK Query</li>
              <li>Developed collaboratively with a group, focusing on inclusivity and Agile methodologies</li>
              <li>Deployed using a cloud provider on the backend and Gitlab Pages for the frontend.</li>
            </ul>
          </p>
          <p>
            <b>Full Stack Developer | Calends-Online |  React, Python, FastAPI, Azure</b>
            <ul>
              <li>Implemented React front-end using date, checkbox, and select inputs and dynamically visible HTML objects to build a class schedule template</li>
              <li>Saved user time and effort when generating a syllabus by automating the data entry process using Python requests library for web scraping & Beautiful Soup library for handling HTML inputs</li>
            </ul>
          </p>
          <p>
            <b>Service Engineer | Dealer's Choice | React, Python, Django</b>
            <ul>
              <li>Presented a user-friendly dashboard as a React-based one-page web application</li>
              <li>Created stateful components to handle Autos, Errors, Sales, etc. and implemented filtering of Services by VIN to provide users with important information easily and quickly</li>
            </ul>
          </p>
          <p>
            <b>Data Analyst | Health Outcomes for Horses | Python</b>
            <ul>
              <li>Processed and cleaned data using Python for data mining and manipulation to increase accuracy and performance of machine learning models</li>
              <li>Used various Python libraries: Numpy, Pandas, Statistics and machine learning models: LightGBM, XGBoost, Sklearn to understand the data and predict individual outcome</li>
            </ul>
          </p>
          <hr/>
          <h4>Education</h4>
          <p>
            <b>Advanced Software Engineering Immersive Program | Hack Reactor</b>
            <ul>
              <li>Built running applications based on software requirements</li>
              <li>Learned and applied Domain Driven Design</li>
              <li>Deployed near-real-time applications using SQL and FastAPI</li>
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
            <b>Field Engineer | Insituform Technologies</b>
            <ul>
              <li>Designed standard operating procedures using production data and statistical methods, including Six Sigma</li>
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
