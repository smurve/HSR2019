# Designing the Architecture of an ML System

The lecture shall elaborate the architecture from ground up by looking at the problems that are to be solved.

**Data-Driven**: Data-driven means fact-driven. The difficulty comes with size and speed of data that don't immediately provide
actionable insight. Computers will help us understand data by means of descriptive analytics and act upon it automatically or 
suggest actions for a human to perform. We'll focus on the latter.

**Question**: What would be the perfect infrastructure to support ML-powered smart functions with high efficiency in developing
and running the algorithms, high quality of data and code and all artifacts, and transparency of conduct?

#### Governing Principles
- Least Effort: The overall operations shall come with the least effort in the long term.
- Transparency of Conduct: We need to be able to tell for sure what's happening with what data at any point in time, 
and why it does so.
- Efficient Maintenance: We want to be able to identify and change a failing algorithm quickly with minimum effort.
- Verify Value Creation (!!!): We want to know for sure the effort's worth it.
- Algorithms need Supervisors: No Algorithm should ever run without monitoring its KPIs
