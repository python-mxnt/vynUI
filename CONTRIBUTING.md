# About Contributing

****If you want to contribute to vynUI, please do as it will help us and the production of vynUI.****

## How to Contribute

## Step 1: How to fork

1. Navigate to the original repository on [GitHub](https://github.com/python-mxnt/vynUI).

2. In the top-right corner of the page, click the Fork button.

3. Choose your personal account as the owner of the fork and click Create fork.

## Step 2: Create local copy of fork on computer

**Cloning creates a local copy of your fork on your computer, allowing you to edit the files.**

1. Navigate to your new fork on GitHub.

2. Click the green Code button and copy the URL (either HTTPS or SSH).

3. Open a terminal or command prompt on your computer.

4. Navigate to where you want to store the project.

5. Run the following command, replacing the URL with the one you copied:

```sh
git clone <your-fork-url>
```

## Step 3: Pull updates from the original repository

**To keep your fork up-to-date, you need to sync it with the original (or "upstream") repository. This ensures you are working with the latest version of the project.**

1. First, change your directory to the project folder you just cloned.

```sh
cd <repo-name>
```

2. Add the original repository as a new remote, which is typically called upstream.

```sh
git remote add upstream <original-repo-url>
```

3. Fetch the latest changes from the original repository.

```sh
git fetch upstream
```

4. Merge the changes from the upstream main (or master) branch into your local branch.

```sh
git merge upstream/main
```

## Step 4: Push your local changes

**After making and committing changes on your local machine, you will push them to your fork on GitHub.**

1. Make your desired changes to your contribution
2. Stage your changes.

```sh
git add .
```

3. **Commit** your changes with a descriptive message.

```sh
git commit -m "Your commit message here"
```

4. Push your committed changes to your fork (the origin remote).

```sh
git push origin <your-branch-name>
```

## Step 5: Create a pull request (PR)

**A pull request is how you ask the original project's maintainers to merge your changes into their repository.**

1. Navigate to your forked repository on GitHub.

2. Above the list of files, you will see a banner with a "Compare & pull request" button.
Click it.

3. Alternatively, click the Pull Requests tab and select New pull request.

4. Use the dropdown menus to compare your fork's branch with the original repository's main branch.

5. Add a clear title and description for your pull request. Explain the changes you made and why.

6. Click Create pull request. vynUI's project maintainers will review your submission and decide whether to merge it.
