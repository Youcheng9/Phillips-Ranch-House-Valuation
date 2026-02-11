# Phillips Ranch Home Valuation Model
A data science project that estimates the fair market value of single-family homes in Phillips Ranch (ZIP 91766) and determines whether a property is overvalued, undervalued, or fairly priced.
Built using XGBoost, deployed with Streamlit, and evaluated using cross-validation.

phillipsranch.streamlit.app

## Project Overview
- The model is trained exclusively on:
  - Single-family residences
  - Phillips Ranch (ZIP 91766)
  - Cleaned and engineered housing data

- The final application allows users to:
  - Input property features
  - View estimated fair value
  - See pricing difference vs listing
  - Get a valuation label (Overvalued / Undervalued / Fairly Priced)
 
### Limitations
This model does not include:
- Interior condition
- Renovation status
- Lot size
- Garage spaces
- Market timing (sale date)

Because of this, the model provides an estimate based solely on structural features and should not be treated as a formal appraisal.
