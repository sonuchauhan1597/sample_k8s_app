from flask import Flask, request, jsonify

app = Flask(__name__)

# Sum of Even Fibonacci Numbers
def sum_even_fibonacci():
    even_sum = 0
    a, b = 0, 1
    count = 0
    while count < 100:
        a, b = b, a + b
        if a % 2 == 0:
            even_sum += a
            count += 1
    return even_sum

# Intersection of Sorted Arrays
def intersection_sorted_arrays():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [3, 4, 5, 6, 7]
    return list(set(arr1) & set(arr2))

# Decimal Digit Transformation
def decimal_digit_transformation():
    x = 3
    return x + int(f"{x}{x}") + int(f"{x}{x}{x}") + int(f"{x}{x}{x}{x}")

# Text Manipulation
def text_manipulation():
    return "Example text manipulation output."

# Route for running operations
@app.route('/run', methods=['GET'])
def run_operation():
    operation = request.args.get('operation')
    if operation == "sum_even_fibonacci":
        result = sum_even_fibonacci()
    elif operation == "intersection_sorted_arrays":
        result = intersection_sorted_arrays()
    elif operation == "decimal_digit_transformation":
        result = decimal_digit_transformation()
    elif operation == "text_manipulation":
        result = text_manipulation()
    else:
        return jsonify({"error": "Invalid operation"}), 400
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
