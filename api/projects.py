# flake8: noqa
PROJECTS = [
    {
        "src": "./img/canarydevs_dashboard.png",
        "alt": "Birddex screenshot",
        "name": "Birddex",
        "id": "birddex",
        "description": "A life-list app for birders.",
        "stack": "Stack: Bootstrap, React Redux, RTK Query, FastAPI, PostgreSQL",
        "body": """
        <a href="https://gitlab.com/canarydevs/birddex">Gitlab Link</a>
        <a href="https://canarydevs.gitlab.io/birddex">Live Site</a>
        <ul>
          <li>
            <p>
            <b>The Pitch:</b>  Log into our app to see a record of all of your sightings of any bird on our app (currently 333 North American species). Sightings include the bird's common name, location and geographic coordinates along with a retrieved via url link. Go to the Birds List and view all of the species  in our database with the ability to search by name or filter by sighted status.
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> We created a PostgreSQL database, a Python FastAPI backend, and a Javascript React frontend. We fill our database of birds and images with data from Nuthatch API and we use Google Geocode and eBirds 2.0 API to retrieve and display observations nearby to the user.
            </p>
          </li>
          <ul>
          <li>
            <p>
            Users can log into individual accounts using JWT authentication, and once authorized can record and review a list of personal bird sightings stored in the SQL server.
            </p>
          </li>
          <li>
            <p>Frontend data is handled via Redux and RTK Query states.</p>
          </li>
          <li>
            <p>Full CRUD operations are available for the sightings API.</p>
          </li>
          <li>
            <p>
            We built the app using Git for version control, and we deployed using cloud hosting and Gitlab Pages.
            </p>
          </li>
          </ul>
          <li>
            <p><b>The Experience:</b> I had several learning opportunities on this project. I had to tackle several new programming challenges throughout, but most importantly, I learned a lot about teamwork and programming in a group.
            </p>
          </li>
          <ul>
          <li>
            <p><b>It was an eye-opening experience both on what I bring to the table in a software development team, and also how the classroom format ties my hands.</b>
                I struggled for a time with my role in the project: I had a strong vision and understood all the parts in the process we would need to complete the project. But this was not my own project, and everyone needed to have a hand in creating it. I very much wanted to take ownership and direct the others, and I feel that was needed, but I didn't want to limit their ownership because this was a class project, not real life. I also held back in critiquing and instructing at times because I didn't want to override their learning experiences. </p>
              </li>
            </ul>
            </ul>
        """
    },
    {
        "src": "./img/calends.png",
        "alt": "Calends screenshot",
        "name": "Calends Online",
        "id": "calends",
        "description": "A syllabus-builder for college classes.",
        "stack": "Stack: Bootstrap, React, FastAPI, Azure Cloud App",
        "body": """
        <a href="https://github.com/jonalfarlinga/calends-online">Github Link</a>
        <a href="https://calends.azurewebsites.net">Live Site</a>
        <a href="https://github.com/jonalfarlinga/calends">Github Link - Terminal App</a>
        <ul>
          <li>
            <p>
            <b>The Pitch:</b> Class starts next week, and you haven't created a syllabus yet. You need to get it done, but just building the table is such a  hassle. Open a text editor and a calendar. You start filling in the dates, but was Spring break the 13th or the 15th? Now bust out the Academic Calendar and verify the holidays that fall on your class periods. Oh yeah, you don't have class on Monday, so take out the MLK holiday!
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> I first created a terminal app using Python's BeautifulSoup library.  The app would scrape the institution's web site for academic calendar data and use that to create a .docx output which includes a table of class meeting dates with holidays filled in.
            </p>
          <ul>
          <li>
            <p>
                I then ported the code to a React and Django full-stack app. I later rebuilt the app using FastAPI for the backend. The current iteration of Calends-Online doesn't need a database or authorization, so it made more sense to serve the API through FastAPI with only the Python logic and the API router.
                On the web, I build and render a table in HTML, which the user can highlight and copy into their favorite text editor. The table is created in an otherwise invisible div and rendered when it becomes relevant.
            </p>
          </li>
          </ul>
          </li>
          <li>
            <p>
                <b>The Experience:</b> This project has a simple front end, but it was incredibly enjoyable practice for backend logic.
            </p>
          <ul>
          <li>
            <p>
                <b>I learned a lot about how I learn.</b> I already knew that I prefer to learn by doing.  When I started using Beautiful Soup, at first I wasn't getting what I expected from my script. After a few attempts at writing code, I decided to open a Python interpreter so that I could quickly iterate through changes in the code. By reviewing docs and attempting several different commands in the interpreter, I gained a thorough knowledge of both BS4 and the webpage I was working with. I realized that while documents can be helpful, I find them much more helpful after I've started using the API and failed a few times.
            </p>
          </li>
          <li>
            <p>
                <b>I like building useful projects.</b> Calends was born of an idle request by a professor I know. She was frustrated with the tedium of creating academic calendars for each class each semester. It was a simple problem that is unreasonably hard to accomplish. Once I presented it to my wife, she was so excited, she told a friend and they both used it immediately. That result was far more reward per effort than any of my previous "for fun" projects.
            </p>
          </li>
        </ul>
        </li>
      <ul>
            """,
    },
    {
        "src": "./img/dealers_choice.png",
        "alt": "Dealer's Choice screenshot",
        "name": "Dealer's Choice",
        "id": "dealers-choice",
        "description": "A car dealership management app.",
        "stack": "Stack: Bootstrap, React, Django, MySQL",
        "body": """
        <a href="https://gitlab.com/dennis.bucklin/dealers-choice">Gitlab Link</a>
        <ul>
          <li>
            <p>
            <b>The Pitch:</b> Dealer's Choice tracks your Autos, Salespeople, Technicians, and Sales. Record your car sales and inventory, and track service appointments and vehicle histories all on our interactive single-page-application! Easily navigate to the information you need through our drop-down nav bar and interactive sales and service lists.
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> This was a pair project with one other teammate. I was responsible for the Auto Service microservice, and my teammate handled the Sales microservice.
            </p>
            <ul>
              <li>
                <p>
                We used Git for version control and sharing dev files.
                </p>
              </li>
              <li>
                <p>
                We built the frontend using React and Bootstrap, and we used JavaScript fetch functions to communicate with the backend.
                </p>
              </li>
              <li>
                <p>
                The backend is built with Python Django and provides a RESTful api for responding to fetch commands. A poller and an automobile Value Object provides an interface between the inventory domain and our microservice domains.
                </p>
              </li>
            </ul>
          </li>
          <li>
            <p>
            <b>The Experience:</b> This project gave me helpful repetitions in writing Javascript code and using React, and it let me experience working together to build a software project.  I also learned about my personal learning and investigation style.
            </p>
          <ul>
          <li>
            <p>
            My partner was absolutely capable and it was excellent working together. We worked separately but shared and worked through issues together.
            </p>
          </li>
          </ul>
          </li>
        </ul>
        """,
    },
    {
        "src": "./img/mlp_dash_screenshot.png",
        "alt": "MLP-Dash screenshot",
        "name": "MLP Dash",
        "id": "mlp-dash",
        "description": "Help Rainbow Dash destroy all of the rain clouds, but watch out for the evil Changelings!",
        "stack": "Stack: Python, Pygame",
        "body": """
        <a href="https://github.com/jonalfarlinga/mlp-dash">Github Link</a>
        <ul>
          <li>
            <p><b>The Pitch:</b> Rainbow Dash is on a mission to clear the skies of all the rain clouds. She's got to be quick, but she's got to be careful. The Changelings are out to get her, and they're not afraid to use the weather against her. Can you help her clear the skies?</p>
          </li>
          <li>
            <p><b>The Work:</b> I built this game using Python and Pygame. I created the game logic using Pygame to handle the display and user input, and I used sprites and sounds borrowed from the internet to provide the content.</p>
            <ul>
              <li>
                <p>Pygame handles the image and sound management, and also handles the sprite position and collision detection.</p>
              </li>
              <li>
                <p>I used object-oriented design, creating player, cloud, and enemy sprites as separate objects.</p>
              </li>
              <li>
                <p>I developed a process whereby the clouds change to a cloudburst image for a moment before disappearing.</p>
              </li>
            </ul>
          </li>
          <li>
            <p><b>The Experience:</b> This project was a lot of fun to build. I learned a lot about game design and development, and I learned a lot about Python and Pygame.</p>
            <ul>
              <li>
                <p><b>It's important to think about the data management in a game.<b> I had to learn how to manage game state and game objects. As I built this project, I went back and forth on whether to separate entities into their own files. I also considered collapsing entities into one class, but eventually settled on once class for the player, one for clouds, etc. I learned that deciding on a schema to manage game data is an important step.</p>
              </li>
              <li>
                <p><b>It's important to think about the user experience.</b> I had introduced my daughter to computer games, but she had trouble understanding how to use the mouse. I designed this game to be touch screen and full-screen ready so that she could manage it more easily.</p>
          </li>
        </ul>
        """
    },
    {
        "src": "./img/projektion_screenshot.png",
        "alt": "Projektion screenshot",
        "name": "Projektion",
        "id": "projektion",
        "description": "Track your and your colleague's projects in the Projektion web app.",
        "stack": "Stack: Django, HTML, CSS, Git, Django/HTML Inheritance, plotly",
        "body": """
        <a href="https://gitlab.com/dennis.bucklin/project-alpha-apr">Gitlab Link</a>
        <ul>
          <li>
            <p><b>The Pitch:</b> Projektion is a project management app. You can create projects, add tasks, and assign them to users. You can view project tasks in list form or Gantt view and manage task status.</p>
          </li>
          <li>
            <p><b>The Work:</b> This was my first major poroject using Git and Django. I used Django/HTML and CSS to render the frontend, and inherited pages using Django/HTML. I built the data and views in Django's framework and used plotly to present the Gantt charts.</p>
          </li>
          <li>
            <p><b>The Experience:</b> I was excited to get started with full stack developement. I cut my teeth on CSS here, and made some important discoveries.</p>
            <ul>
              <li>
                <p><b>I can always check the computed size of an object.</b> I had set some setting for object size that resulted in the page rendering with an extra white border around the right and bottom corner of the screen. I struggled with settings until I used the dev tools to inspect each element, which revealed that the footer was bigger than intended and stretched the viewport outsidthe border fo the page. This was incredibly helpful later in creating my portfolio page.</p>
              </li>
            </ul>
          </li>
        </ul>
        """
    }
]
