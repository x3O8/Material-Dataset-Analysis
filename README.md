# Material-Dataset-Analysis
Analysis of Material Datasets to find trends based on composition

## Abstract
The integration of data science with material science has revolutionized the understanding and optimization of material properties. This study focuses on the analysis of carbon steel properties based on its grade, utilizing a correlation matrix to uncover the relationships between mechanical properties such as ultimate tensile strength (UTS), yield strength (YS), hardness, and ductility, as well as chemical compositions including carbon and manganese content. The objective is to identify significant trends and correlations that can guide material selection and design. 

Datasets for carbon steel were collected from publicly available sources and lab experiments, followed by rigorous data processing and cleaning to ensure accuracy and consistency. Features such as UTS, YS, hardness, elongation, and chemical compositions were extracted and standardized. Statistical methods were then employed to construct a correlation matrix, quantifying the strength and direction of relationships between the various properties. Pearson correlation coefficients were calculated, with the results visualized in a heatmap for easy interpretation. This approach enabled a comprehensive analysis of how different properties interrelate, providing a robust framework for understanding material behavior. 

The results reveal strong positive correlations between the grade of carbon steel and its UTS, YS, and hardness, indicating that higher grades are associated with increased strength and hardness. Conversely, a negative correlation was observed between grade and ductility measures such as elongation and reduction of area, suggesting that higher-grade steels are less ductile. Also, carbon content significantly impacted the mechanical properties, correlating positively with strength and hardness. These findings underscore the critical role of chemical composition in determining the mechanical properties of carbon steel and highlight the value of material informatics, enhanced by meticulous data processing and feature extraction, in advancing material science. 


## Introduction

Material informatics leverages data science techniques to extract knowledge from material datasets, offering insights into the properties and compositions of various materials. By analyzing large datasets, it facilitates the discovery of meaningful patterns and correlations, leading to improved material selection and design. 

Carbon steel’s mechanical properties, such as ultimate tensile strength (UTS), yield strength (YS), hardness, and ductility, are influenced by its chemical composition, including the contents of carbon, manganese, phosphorus, and sulfur. Identifying the interdependencies among these properties is crucial for developing high-performance materials. This research employs a correlation matrix to systematically explore these relationships, providing insights that can guide the selection and development of carbon steel grades tailored to specific applications. 

To achieve this, datasets were gathered from publicly available sources and laboratory experiments, followed by rigorous data processing, cleaning, and feature extraction. Statistical methods were used to construct a correlation matrix, highlighting the strength and direction of relationships between the properties. The resulting analysis offers a comprehensive understanding of how different mechanical properties and chemical compositions of carbon steel interrelate, underscoring the value of material informatics in advancing material science. 

 
## Results and Discussions

The analysis of carbon steel properties reveals significant relationships between its mechanical properties and grade, as illustrated by the provided visualizations and correlation matrix. The trends observed in these graphs offer a deeper understanding of how different mechanical properties vary with changes in grade. 

#### Fig 3.1. Correlation Matrix  

The correlation matrix offers a quantitative overview of the relationships between various properties of carbon steel. Key observations include: 

Ultimate Tensile Strength (UTS) and Hardness (HB): Both UTS (in MPa and Ksi) and hardness (HB) show very high positive correlations with the grade of carbon steel (0.94), indicating that as the grade increases, both UTS and hardness significantly improve. This is confirmed by the perfect correlation between UTS and hardness (correlation coefficient of 1.0), reflecting that harder steels are inherently stronger. 


Yield Strength (YS): Yield strength (both in MPa and Ksi) also shows a strong positive correlation with the grade (0.63), UTS (0.76), and hardness (0.75), signifying that higher-grade steels exhibit higher yield strength. 

Ductility Measures (Elongation and Reduction of Area): Both elongation (%) and reduction of area (%) exhibit strong negative correlations with grade (-0.77 and -0.61, respectively), UTS (-0.87 and -0.75, respectively), and YS (-0.91 and -0.56, respectively). This indicates that as the strength and hardness of carbon steel increase with grade, its ductility decreases. 

#### Fig 3.2. Yield Strength and UTS  

Yield Strength and Ultimate Tensile Strength 

Fig 3.2 shows the trends of yield strength (YS) and ultimate tensile strength (UTS) across different grades: 

Yield Strength (YS): The blue line displays an upward trend with significant fluctuations, suggesting variability within the samples but an overall increase from around 200 MPa to 500 MPa as the grade increases. 

Ultimate Tensile Strength (UTS): The orange line exhibits a consistent upward trend, reaching up to 800 MPa, reinforcing the strong positive correlation with the grade. 

These trends confirm the correlation matrix findings, where higher grades are associated with higher tensile and yield strengths. 

#### Fig 3.3. Graph of Elongation and Reduction 

 

#### Fig 3.4. Graph of Hardness against Steel Grade 

Elongation and Reduction of Area 

Fig 3.3 illustrates how elongation (%) and reduction of area (%) vary with the grade: 

Elongation (%): The blue line demonstrates a clear downward trend, indicating a decrease from approximately 30% to 10% as the grade increases, highlighting reduced ductility in higher-grade steels. 

Reduction of Area (%): Similarly, the orange line decreases from about 55% to 30%, further indicating that higher grades are less ductile. 

These visual trends align with the negative correlations observed in the matrix, showing that higher strength and hardness come at the expense of ductility. 

### Comprehensive Insights 

Strength vs. Ductility Trade-off: The combined data indicate a clear trade-off between strength and ductility in carbon steels. Higher-grade steels exhibit significantly higher UTS, YS, and hardness, making them suitable for applications demanding high strength and wear resistance. However, this enhancement in mechanical strength reduces ductility, which may limit their use in applications where flexibility and deformation capacity are critical. 

Impact of Chemical Composition: The strong correlations between carbon content (c_min and c_max) and mechanical properties like UTS, YS, and hardness underscore the vital role of chemical composition in determining the material's performance. Higher carbon content enhances strength and hardness but also contributes to decreased ductility, aligning with the observed trade-offs. 
 
 

 
 
