import streamlit as st
from fractions import Fraction

def parse_fraction(input_str):
    """Convert string input to fraction"""
    if not input_str:  # Handle empty input
        return None
    try:
        if '/' in input_str:
            if ' ' in input_str:  # Mixed number
                whole, frac = input_str.split()
                return Fraction(whole) + Fraction(frac)
            return Fraction(input_str)
        return Fraction(int(input_str))
    except:
        return None

def format_fraction(frac):
    """Format fraction for display"""
    if frac is None:
        return ""
    if frac.denominator == 1:
        return str(frac.numerator)
    if abs(frac) >= 1:
        whole = int(frac)
        frac_part = abs(frac - whole)
        if frac_part == 0:
            return str(whole)
        return f"{whole} {frac_part}"
    return str(frac)

# Page configuration
st.set_page_config(page_title="Frame Calculator", layout="centered")

# Title and instructions
st.title("🖼️ Frame Calculator")
st.markdown("""
### Input Instructions
Enter measurements in any of these formats:
- Whole numbers (e.g., 8)
- Fractions (e.g., 1/2)
- Mixed numbers (e.g., 8 1/2)
""")

# Create a form for inputs
with st.form("frame_calculator_form"):
    # Create two columns for inputs
    col1, col2 = st.columns(2)
    
    with col1:
        art_width = st.text_input("Art Width (inches)", placeholder="e.g., 8 1/2")
        rabbet_depth = st.text_input("Rabbet Depth (inches)", placeholder="e.g., 1/4")
    
    with col2:
        art_length = st.text_input("Art Length (inches)", placeholder="e.g., 11")
        frame_width = st.text_input("Frame Width (inches)", placeholder="e.g., 2")

    # Submit button
    submitted = st.form_submit_button("Calculate Dimensions", use_container_width=True)

# Process calculations when form is submitted
if submitted:
    # Convert inputs to fractions
    width = parse_fraction(art_width)
    length = parse_fraction(art_length)
    rabbet = parse_fraction(rabbet_depth)
    frame = parse_fraction(frame_width)
    
    if all([width, length, rabbet, frame]):  # Check if all inputs are valid
        # Constants
        WIGGLE_ROOM = Fraction(1, 16)  # 1/16 inch
        
        # Calculations
        opening_width = width + (WIGGLE_ROOM * 2)
        opening_length = length + (WIGGLE_ROOM * 2)
        
        outside_width = opening_width - (rabbet * 2) + (frame * 2)
        outside_length = opening_length - (rabbet * 2) + (frame * 2)
        
        # Display results in a nice format
        st.success("Calculations completed!")
        
        # Create three columns for results
        st.markdown("### Results")
        result_col1, result_col2, result_col3 = st.columns(3)
        
        with result_col1:
            st.markdown("**Art Size**")
            st.markdown(f"{format_fraction(width)} × {format_fraction(length)}\"")
            
        with result_col2:
            st.markdown("**Opening Size**")
            st.markdown(f"{format_fraction(opening_width)} × {format_fraction(opening_length)}\"")
            
        with result_col3:
            st.markdown("**Outside Size**")
            st.markdown(f"{format_fraction(outside_width)} × {format_fraction(outside_length)}\"")
        
        # Add explanation
        st.markdown("---")
        with st.expander("See calculation details"):
            st.markdown("""
            - Opening size includes 1/16" wiggle room on each side
            - Outside size accounts for rabbet depth and frame width
            - All measurements are in inches
            """)
    else:
        st.error("Please enter valid measurements in all fields")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit • [Report an Issue](https://github.com)")
