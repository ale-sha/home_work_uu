import unittest
import tests_12_2
import test_runner

run_test = unittest. TestSuite()
loader = unittest.TestLoader()

run_test.addTest(loader.loadTestsFromTestCase(tests_12_2.TournamentTest))
run_test.addTest(loader.loadTestsFromTestCase(test_runner.RunnerTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_test)


