# Project C: Exploratory Dashboard of Cost of Living and Living Wages
Joshua Nielsen  
Prof. Mike Ryu  
CS-150 Community Action Computing  

![Screenshot of the visualizer in action](/assets/Sample_Screenshot.png)

## Thesis Statement
I want to create a dashboard people can use to consider the cost of living in California. I want to provide accurate, helpful data while leaving it wide open for exploration and discovery.

## Region of Choice
California is known for being one of the most expensive states to live in. It is also the state I have lived in for my entire life. If I want to keep living here and start a family, I am going to have to get a great job. But how much do I have to make? This dashboard answers that question.

## What am I Visualizing?
I am visualizing two different datasets. One is median household income for the state of California, which I accessed via the FRED (Federal Reserve Economic Data) website. The other is a price table of several essentials from the U.S. Bureau of Labor Statiscis, which I plugged into my own special algorithm to calculate annual expenses for households of varying size. You can read more about the datasets and see their citations in the "permissions" tab of the applicaiton!

## Data Visualization Strategies
The line graphs I use in this application are fairly straightforward, though there is a lot of depth to them. They each take multiple elements of user input into account, many of which have default/automatically adjusting values for ease of use. I make sure that there is enough space between elements that the users are not overwhelmed, and I keep the amount of colors fairly low (the one exception being the expenses graph) for the same reason. I made a little visual for the size of the household/working adults to help the user grasp the scale of their situation. Several elements will only be visible/factored into calculations when they are relevant, (i.e. multiple working adults, savings) removing some clutter from the system.

## Example Scenarios
1. The working adult(s) in a California household want to compare their annual income to the recommended number to see if they are earning enough
2. The working adult(s) in a California household want to check their annual income to see how many dependents they can support.
3. The working adult(s) in a California household want to see how much money they can save up annually and still cover their expenses.
