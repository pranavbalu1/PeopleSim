<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Population Simulation Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #bbb 1px solid;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 24px;
        }
        code {
            background: #eee;
            padding: 2px 4px;
            border-radius: 4px;
        }
        h2 {
            border-bottom: 2px solid #333;
            padding-bottom: 5px;
        }
        ul {
            margin: 0;
            padding: 0;
            list-style: none;
        }
        ul li {
            margin-bottom: 10px;
        }
        pre {
            background: #eee;
            padding: 10px;
            border: 1px solid #ccc;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Population Simulation Project</h1>
        </div>
    </header>

    <div class="container">
        <section>
            <h2>Overview</h2>
            <p>This project simulates the behavior of individuals in a city, including job opportunities, education, and housing. It includes features for managing agents, companies, and properties, and allows you to visualize simulation results using Streamlit.</p>
        </section>

        <section>
            <h2>Project Structure</h2>
            <pre><code>
PeopleSim/
│
├── city/
│   ├── __init__.py
│   ├── city.py
│
├── agents/
│   ├── __init__.py
│   ├── agent.py
│
├── laws/
│   ├── __init__.py
│   ├── tax_law.py
│
├── config/
│   ├── config.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
            </code></pre>
        </section>

        <section>
            <h2>Requirements</h2>
            <p>To run this project, you'll need Python 3.10 or higher. Install the required packages using <code>pip</code>:</p>
            <ol>
                <li>Create a virtual environment (recommended):
                    <pre><code>python3 -m venv venv</code></pre>
                </li>
                <li>Activate the virtual environment:
                    <ul>
                        <li><strong>On Windows:</strong>
                            <pre><code>venv\Scripts\activate</code></pre>
                        </li>
                        <li><strong>On macOS/Linux:</strong>
                            <pre><code>source venv/bin/activate</code></pre>
                        </li>
                    </ul>
                </li>
                <li>Install the required packages:
                    <pre><code>pip install -r requirements.txt</code></pre>
                </li>
            </ol>
        </section>

        <section>
            <h2>Installation</h2>
            <ol>
                <li>Clone the repository:
                    <pre><code>git clone &lt;repository-url&gt;</code></pre>
                </li>
                <li>Navigate to the project directory:
                    <pre><code>cd PeopleSim</code></pre>
                </li>
                <li>Set up the virtual environment and install dependencies (as described in the Requirements section).</li>
            </ol>
        </section>

        <section>
            <h2>Usage</h2>
            <ol>
                <li><strong>Run the Simulation</strong>
                    <p>To run the simulation, execute the <code>main.py</code> script:</p>
                    <pre><code>python main.py</code></pre>
                    <p>This will start the simulation and save the results to <code>simulation_results.csv</code>.</p>
                </li>
                <li><strong>Visualize Data with Streamlit</strong>
                    <p>To visualize simulation results using Streamlit, first ensure Streamlit is installed:</p>
                    <pre><code>pip install streamlit</code></pre>
                    <p>Then, run the Streamlit app:</p>
                    <pre><code>streamlit run visualization.py</code></pre>
                    <p>This will open a web interface where you can view trends and specific agent data.</p>
                </li>
            </ol>
        </section>

        <section>
            <h2>File Descriptions</h2>
            <ul>
                <li><strong><code>city/city.py</code></strong>: Contains the <code>City</code>, <code>Property</code>, and <code>Company</code> classes, managing city properties and companies.</li>
                <li><strong><code>agents/agent.py</code></strong>: Contains the <code>Agent</code> class, representing individuals in the simulation, including their jobs and education.</li>
                <li><strong><code>laws/tax_law.py</code></strong>: Defines functions related to tax laws and their effects on agents.</li>
                <li><strong><code>config/config.py</code></strong>: Contains configuration settings for the simulation.</li>
                <li><strong><code>main.py</code></strong>: The entry point for running the simulation.</li>
                <li><strong><code>visualization.py</code></strong>: Streamlit app for visualizing simulation data.</li>
            </ul>
        </section>

        <section>
            <h2>Contributing</h2>
            <p>Feel free to open issues or submit pull requests if you have improvements or bug fixes. Please make sure to follow the project's code style and testing practices.</p>
        </section>

        <section>
            <h2>License</h2>
            <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
        </section>

        <section>
            <h2>Contact</h2>
            <p>For questions or further information, please contact <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>
        </section>
    </div>
</body>
</html>
