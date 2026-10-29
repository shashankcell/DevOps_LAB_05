# Experiment 05 — Team collaboration with branches and pull requests

**Student:** [Your name]  
**Register number:** [Your register number]  
**Course:** Collaborative Development and DevOps

## Aim

Use a fork-based workflow to make a change on a feature branch and submit it for review through a pull request.

## Procedure

1. Open the reference repository or another repository you are authorized to use. Choose **Fork** on GitHub to create a fork under your account. Do not push directly to someone else's repository.
2. Clone your fork and register the original as the `upstream` remote:
   ```sh
   git clone https://github.com/YOUR-USER/YOUR-FORK.git
   cd YOUR-FORK
   git remote add upstream https://github.com/ORIGINAL-OWNER/ORIGINAL-REPO.git
   git remote -v
   ```
3. Create a feature branch and make a small, useful change:
   ```sh
   git switch -c feature/team-note
   printf "\nContribution workflow demo.\n" >> README.md
   git add README.md
   git commit -m "Add team workflow note"
   git push -u origin feature/team-note
   ```
4. On GitHub, open a pull request from your fork's `feature/team-note` branch to the upstream repository's `main` branch. Describe the change and review the diff before submitting.
5. After review, synchronize your local main branch:
   ```sh
   git switch main
   git fetch upstream
   git merge upstream/main
   git push origin main
   ```

## What to record

Record the fork URL, branch name, and pull-request link if you are authorized to submit one. A pull request to another person's project is optional; you can practice with two repositories you own. Explain the difference between `origin` and `upstream`.

## Result

Complete this section after performing the workflow. Do not claim a pull request was accepted unless it was.

## Reference and attribution

The topic follows the collaboration, fork, and pull-request theme in [Smirk1308/DevOps_LAB_05](https://github.com/Smirk1308/DevOps_LAB_05). The sample procedure is independently authored.