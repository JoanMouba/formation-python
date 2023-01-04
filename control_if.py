# code pour les conditions
test_name = "ui_test_001"
test_category = "UI_TESTS"

if test_name == "ui_test_001":
  print("Test found")

if test_name == "ui_test_034":
  print("Test not found")
else:
  print("Implement the test")

if test_name == "ui_test_034":
  print("Test not found")
elif test_name == "ui_test_143":
  print("Implement the test")
elif test_name == "ui_test_215":
  print("Implement the test")
else:
  print("Test not required")

if test_name == "ui_test_001":
  if test_category == "UI_TESTS":
    print("Test found")
  else:
    print("Test is of another type")
elif test_name == "ui_perf_219":
  if test_category == "PERFORMANCE_TESTS":
    print("Test found")
else:
  print("Implement the test")
 
