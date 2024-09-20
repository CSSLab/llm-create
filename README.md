# Human Creativity in the Age of LLMs: Randomized Experiments on Divergent and Convergent Thinking

## Running the Interfaces
1. Navigate to the interface directory
2. Download dependencies by running `npm install`
3. Launch the React application in development mode by running `npm start`

## Running the Convergent Analysis
1. Navigate to the `convergent/analysis/` directory
2. Install necessary packages with
   ```
   install.packages(c("tidyverse", "scales", "here", "knitr", "gridExtra", "patchwork", "reshape2", "lmerTest", "emmeans", "dplyr", "broom", "ggbeeswarm", "ggpubr", "rstatix"))
   ```
4. Run
   ```
   rmarkdown::render("convergent-analysis.Rmd")
   ```

## Running the Divergent Analysis
1. Navigate to the `divergent/analysis` directory
2. Open the `ipynb` file and set up the correct csv file paths
