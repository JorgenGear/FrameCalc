from fractions import Fraction

def parse_fraction(input_str):
    """Convert string input to fraction (handles mixed numbers like '1 1/2')"""
    try:
        # First try converting as a simple fraction or integer
        return Fraction(input_str)
    except ValueError:
        try:
            # Try handling mixed number (e.g., "1 1/2")
            whole, frac = input_str.split()
            return Fraction(whole) + Fraction(frac)
        except:
            raise ValueError("Invalid input. Please use format: '1/2' or '1 1/2'")

def format_fraction(frac):
    """Convert fraction to mixed number string format"""
    # If it's a whole number, return it as an integer
    if frac.denominator == 1:
        return str(frac.numerator)
    
    # Convert to mixed number if greater than 1
    if abs(frac) >= 1:
        whole = int(frac)
        frac_part = abs(frac - whole)
        if frac_part == 0:
            return str(whole)
        return f"{whole} {frac_part}"
    return str(frac)

def calculate_frame_dimensions():
    print("\nFrame Measurement Calculator")
    print("-" * 30)
    print("Enter measurements as fractions (e.g., '1/2' or '1 1/2')")
    
    # Get art piece dimensions
    try:
        art_width = parse_fraction(input("Enter art piece width (inches): "))
        art_length = parse_fraction(input("Enter art piece length (inches): "))
        rabbet_depth = parse_fraction(input("Enter rabbet depth (inches): "))
        frame_width = parse_fraction(input("Enter frame width (inches): "))
    except ValueError as e:
        print(f"Error: {e}")
        return None
    
    # Constants
    WIGGLE_ROOM = Fraction(1, 16)  # 1/16 inch
    
    # Calculate opening size (including wiggle room)
    opening_width = art_width + (WIGGLE_ROOM * 2)
    opening_length = art_length + (WIGGLE_ROOM * 2)
    
    # Calculate outside dimensions
    outside_width = opening_width - (rabbet_depth * 2) + (frame_width * 2)
    outside_length = opening_length - (rabbet_depth * 2) + (frame_width * 2)
    
    # Display results
    print("\nCalculated Frame Dimensions:")
    print("-" * 30)
    print(f"Art Piece Size: {format_fraction(art_width)} x {format_fraction(art_length)}")
    print(f"Frame Opening Size: {format_fraction(opening_width)} x {format_fraction(opening_length)}")
    print(f"Outside Frame Dimensions: {format_fraction(outside_width)} x {format_fraction(outside_length)}")
    
    return outside_width, outside_length

if __name__ == "__main__":
    while True:
        result = calculate_frame_dimensions()
        if result is None:
            print("Please try again with valid measurements.")
        
        again = input("\nCalculate another frame? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Frame Calculator!")
            break
