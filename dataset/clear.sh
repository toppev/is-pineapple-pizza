# Clear dataset directories

rm -r training_set
mkdir training_set
mkdir training_set/not_pineapple
mkdir training_set/pineapple
touch training_set/not_pineapple/.gitkeep
touch training_set/pineapple/.gitkeep

rm -r test_set
mkdir test_set
mkdir test_set/not_pineapple
mkdir test_set/pineapple
touch test_set/not_pineapple/.gitkeep
touch test_set/pineapple/.gitkeep