PROJECTS = [
    {
        "src": "./img/canarydevs_dashboard.png",
        "alt": "Birddex screenshot",
        "name": "Birddex",
        "id": "birddex",
        "description": "A life-list app for birders.",
        "stack": "Stack: Bootstrap, React Redux, \
            RTK Query, FastAPI, PostgreSQL",
        "body": """
        <ul>
          <li>
            <p>
            <b>The Pitch:</b>  Log into our app to see a record of all of your\
             sightings of any bird on our app (currently 333 North American \
            species). Sightings include the bird's common name, location and \
            geographic coordinates along with a retrieved via url link. Go to \
            the Birds List and view all of the species  in our database with \
            the ability to search by name or filter by sighted status.
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> We created a PostgreSQL database, a Python \
                FastAPI backend, and a Javascript React frontend. We fill our \
                database of birds and images with data from Nuthatch API and \
                we use Google Geocode and eBirds 2.0 API to retrieve and \
                display observations nearby to the user.
            </p>
          </li>
          <ul>
          <li>
            <p>
            Users can log into individual accounts using JWT \
            authentication, and once authorized can record and review a list \
            of personal bird sightings stored in the SQL server.
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
            We built the app using Git for version control, and we deployed \
            using cloud hosting and Gitlab Pages.
            </p>
          </li>
          </ul>
        </ul>
        <ul>
          <li>
            <p><b>The Experience:</b> I had several learning opportunities on \
                this project. I had to tackle several new programming \
                challenges throughout, but most importantly, I learned a lot \
                about teamwork and programming in a group.
            </p>
          </li>
          <li>
            <p><b>It was an eye-opening experience both on what I bring to the\
                 table in a software development team, and also how the \
                classroom format ties my hands.</b>
                I struggled for a time with my role in the project: I had a \
                strong vision and understood all the parts in the process we \
                would need to complete the project. But this was not my own \
                project, and everyone needed to have a hand in creating it. \
                I very much wanted to take ownership and direct the others, \
                and I feel that was needed, but I didn't want to limit their \
                ownership because this was a class project, not real life. I \
                also held back in critiquing and instructing at times because \
                I didn't want to override their learning experiences. </p>
              </li>
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
        <ul>
          <li>
            <p>
            <b>The Pitch:</b> Class starts next week, and you haven't created \
                a syllabus yet. You need to get it done, but just building the\
                 table is such a  hassle. Open a text editor and a calendar. \
                You start filling in the dates, but was Spring break the 13th \
                or the 15th? Now bust out the Academic Calendar and verify \
                the holidays that fall on your class periods. Oh yeah, you \
                don't have class on Monday, so take out the MLK holiday!
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> I first created a terminal app using Python's \
                BeautifulSoup library.  The app would scrape the institution's\
                 web site for academic calendar data and use that to create a \
                .docx output which includes a table of class meeting dates \
                with holidays filled in.
            </p>
            <ul>
          <li>
            <p>
                I then ported the code to a React and Django full-stack app. \
                I later rebuilt the app using FastAPI for the backend. The \
                current iteration of Calends-Online doesn't need a database \
                or authorization, so it made more sense to serve the API \
                through FastAPI with only the Python logic and the API router.
                On the web, I build and render a table in HTML, which the user\
                 can highlight and copy into their favorite text editor. The \
                table is created in an otherwise invisible div and rendered \
                when it becomes relevant.
            </p>
          </li>
            </ul>
          </li>
          <li>
            <p>
                <b>The Experience:</b> This project has a simple front end, \
                but it was incredibly enjoyable practice for backend logic.
            </p>
          </li>
          <li>
            <p>
                <b>I learned a lot about how I learn.</b> I already knew that \
                I prefer to learn by doing.  When I started using Beautiful \
                Soup, at first I wasn't getting what I expected from my \
                script. After a few attempts at writing code, I decided to \
                open a Python interpreter so that I could quickly iterate \
                through changes in the code. By reviewing docs and attempting \
                several different commands in the interpreter, I gained a \
                thorough knowledge of both BS4 and the webpage I was working \
                with. I realized that while documents can be helpful, \
                I find them much more helpful after I've started using the \
                API and failed a few times.
            </p>
          </li>
          <li>
            <p>
                <b>I like building useful projects.</b> Calends was born of an\
                 idle request by a professor I know. She was frustrated with \
                the tedium of creating academic calendars for each class each \
                semester. It was a simple problem that is unreasonably hard to\
                 accomplish. Once I presented it to my wife, she was so \
                excited, she told a friend and they both used it immediately. \
                That result was far more reward per effort than any of my \
                previous "for fun" projects.
            </p>
          </li>
      <ul>
            """,
    },
    {
        "src": "./img/dealers_choice.png",
        "alt": "Dealer's Choice screenshot",
        "name": "Dealer's Choice",
        "id": "calends",
        "description": "A car dealership management app.",
        "stack": "Stack: Bootstrap, React, Django, MySQL",
        "body": """
        <ul>
          <li>
            <p>
            <b>The Pitch:</b> Dealer's Choice tracks your Autos, Salespeople, \
            Technicians, and Sales. Record your car sales and inventory, and \
            track service appointments and vehicle histories all on our \
            interactive single-page-application! Easily navigate to the \
            information you need through our drop-down nav bar and interactive\
             sales and service lists.
            </p>
          </li>
          <li>
            <p>
            <b>The Work:</b> This was a pair project with one other teammate. \
            I was responsible for the Auto Service microservice, and my \
            teammate handled the Sales microservice.
            </p>
          </li>
            <ul>
              <li>
                <p>
                We used Git for version control and sharing dev files.
                We built the frontend using React and Bootstrap, and we used \
                JavaScript fetch functions to communicate with the backend
                </p>
              </li>
              <li>
                <p>
                The backend is built with Python Django and provides a RESTful\
                 api for responding to fetch commands. A poller and an \
                automobile Value Object provides an interface between the \
                inventory domain and our microservice domains.
                </p>
              </li>
            </ul>
          <li>
            <p>
            <b>The Experience:</b> This project gave me helpful repetitions in\
             writing Javascript code and using React, and it let me experience\
             working together to build a software project.  I also learned \
            about my personal learning and investigation style.
            </p>
          </li>
          <li>
            <p>
            My partner was absolutely capable and it was excellent working \
            together. We worked separately but shared and worked through \
            issues together.
            </p>
          </li>
        </ul>
        """,
    }
]
