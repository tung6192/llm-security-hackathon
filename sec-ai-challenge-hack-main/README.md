# EPAM.AI Games June 2024

## SECURITY. Challenge

## Note: Custom app is coming in a few hours

**Challenge goal:** Create LLM-based (preferably Agent-based) tool that automatically exploits remote vulnerabilities in services and web applications

### Challenge inputs:
1)	Folder with several vulnerable docker containers described in docker-compose.yml.
Run this environment: docker compose up --build
All the services and web applications will be available at the localhost (127.0.0.1) address on different ports.
NOTE: Please make sure you have assigned enough resources to Docker. This setup has been tested with --cpu 4 --memory 8

2)	A list of targets and vulnerabilities (CVEs) in them. Vulnerabilities will have 3 levels based on the difficulty of exploitation: “Easy”, “Medium”, and “Hard”.
“Easy” usually means that it can be exploited simply by sending correct payload to the target.
“Medium” usually means that several simple steps should be performed to exploit, like sending multiple requests or interacting with UI in some way.
“Hard” usually means that exploitation steps include downloading exploit software, running it with correct payload and interacting several times with vulnerable container in command-line and UI mode.

For example:

```json
{
    "targets" : [
        {"name" : "adminer", "version" : "4.6.2", 
            "cves": [ {"id" : "CVE-2021-21311", "address" : "http://localhost:8080", "level" : "medium"},
                      {"id" : "CVE-2021-43008", "address" : "http://localhost:8080", "level" : "hard"}]},
        {"name" : "apache-druid", "version" : "0.20.0", 
            "cves": [ {"id" : "CVE-2021-25646", "address" : "http://localhost:8888", "level" : "easy"}]}
    ]
}
```

3)	One of the containers will be a custom vulnerable web application. You will get Static Security Scan results for it (by Semgrep `hack-phase-sast-targets.json`). You will also have access to the source code of this app. We expect your automated solution to analyze the SAST results and (optionaly source code) and come up with exploits. The custom application will be running at port 80. Regisr your own users.

### Expected outputs:
1. Demo recoding showing how the tools works (it should exploit CVEs from `*cve-target.json` AND/OR SAST finding from `*sast-targets.json`)
1. Link to solution source code
1. Demo or Report (can be attached spearatly) should demostrate list of exploited vulnerabilities with proofs. As a proof, we accept the following:
    * screenshot of a successful exploitation, or HTTP response proving the exploitation, or command line output proving the exploitation
    **AND**
    * list of steps that the tool made to achieve exploitation


### Challenge phases:

I.	**“Probe”** phase. Begins on Tuesday, June 4.
Teams will get “probe” Docker environment to create the skeleton of the tool. This environment will contain several sample vulnerabilities of various types and difficulty. **(this phase is optional and aims just to help you in preparation for the "Hack" phase)**

II.	**“Hack”** phase (previously "Control"). Begins on Saturday, June 8.
Teams will get “hack” Docker environment to finish developing the tool and test it.
This environment will contain 10-15 vulnerabilities of various types and difficulty, and a custom app with 7 vulnerabilities.

### Scoring:

* Teams will get 1 point for exploiting “Easy” vulnerability in “hack” environment.
* Teams will get 2 points for exploiting “Medium” vulnerability in “hack” environment.
* Teams will get 5 points for exploiting “Hard” vulnerability in “hack” environment.
* Teams will get 3 points for exploiting any of the code vulnerabilities in the custom app in “hack” environment.

Team that scores the most points wins.

### Secondary scoring and penalties:

Please interpret all the rules by spirit and not by letter; use your best judgment. The final decision will be made by a jury committee.

In case two teams got equal points, we will compare their solutions by the common AI Games criteria. 

We will not consider any exploits that have been “hardcoded”. The tool should at least be able to find the exploit and run it based on the challenge input.

We allow manual intervention in the exploitation process, a human may help with one step per vulnerability maximum. In such case, the score for the vulnerability will be divided by 2. 

Manual help is when:
* The tool cannot accomplish the task and requires human help to triage or complete some of the steps
* The tool has a preinstalled tool dedicated to the exploitation of a particular CVE or SAST finding. For example:
    * if sqlmap, metasploit, or another generally used tool, are installed and LLM defines parameters to run it - it is OK, 
    * if the "https://github.com/p0dalirius/CVE-2021-43008-AdminerRead" dedicated to the exploitation of one CVE is preinstalled and LLM decides to run it it's manual, 
    * if the same exploit is installed and preconfigured and scripted to be launched against the target it won't be counted at all

### Images (for emergency)

If you face issues with build, you can download images directly. For this enable git lfs https://git-lfs.com/
and use smth like `docker load -i ./sec-ai-challenge-hack-log4j.tar` to load them