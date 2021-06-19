from math import sqrt
import numpy
import pandas  # type:ignore
import matplotlib.pyplot as plt  # type:ignore
import scipy.stats  # type:ignore


def main(should_plot: bool):
    """Main Wrapper for Lab"""
    ratings_url = (
        "https://cf-courses-data.s3.us.cloud-object-"
        + "storage.appdomain.cloud/IBMDeveloperSkills"
        + "Network-ST0151EN-SkillsNetwork/labs/teachingratings.csv"
    )

    ratings_df = pandas.read_csv(ratings_url)

    x_axis = numpy.arange(-4, 4, 0.1)

    pdf = scipy.stats.norm.pdf(x_axis, 0, 1)
    plt.plot(x_axis, pdf)
    if should_plot:
        plt.show()

    eval_mean = round(ratings_df["eval"].mean(), 3)
    eval_std = round(ratings_df["eval"].std(), 3)
    print(f"Evaluation Mean, StdDev  {eval_mean}, {eval_std}")

    eval_unit = "evaluation score"

    calc_and_print_cdf_right(eval_unit, 4.5, eval_mean, eval_std)

    # Find probability of eval score less than 3.5
    random_var1 = 3.5
    calc_and_print_cdf(eval_unit, random_var1, eval_mean, eval_std)

    calc_and_print_cdf(eval_unit, 4.2, eval_mean, eval_std)

    calc_and_print_cdf_between(eval_unit, eval_mean, eval_std, 3.5, 4.2)

    # H0:
    null_hypothesis = (
        "Mean point of regional players is not different from historic mean"
    )
    # H1: Mean point of regional players is different from historic mean

    historic_mean = 12.0
    historic_std = 5.5
    sample_size = 36
    sample_mean = 10.7
    z_score = calc_sample_z_score(sample_mean, sample_size, historic_mean, historic_std)
    p_value = 0.05

    # Two tail cdf
    z_score_cdf = 2 * scipy.stats.norm.cdf(z_score)
    if z_score_cdf < p_value:
        print(
            f"Since Two-Tail Z Score {z_score_cdf} is less than the P-Value {p_value} we reject the null hypothesis: {null_hypothesis}"
        )
    else:
        print(
            f"Since Two-Tail Z Score {z_score_cdf} is greater than P-Value {p_value} we fail to reject the null hypothesis: {null_hypothesis}"
        )

    # Question 1
    calc_and_print_cdf_right(eval_unit, 3.3, eval_mean, eval_std)

    # Question 2
    calc_and_print_cdf_between(eval_unit, eval_mean, eval_std, 2.0, 3.0)

    # Question 3

    null_hypothesis = "Those who sleep more than 8 hours have an average IQ of 100"
    alernative_hypothesis = (
        "Those who sleep more than 8 hours have an average IQ of greater than 100"
    )

    iq_range = numpy.array([116, 111, 101, 120, 99, 94, 106, 115, 107, 101, 110, 92])
    sample_size = len(iq_range)
    sample_mean = iq_range.mean()
    sample_std = iq_range.std()

    print(f"sample mean {sample_mean}")

    # Probability of Null Hypothesis
    prob = scipy.stats.norm.cdf((sample_mean - 100) / (sample_std / sqrt(sample_size)))
    print(prob)
    # This is a bad question, sample size less than 30, T test more appropriate

    # Probability of True mean of 100 given sample is less than 1 percent therefore
    # We reject the null hypothesis


def calc_sample_z_score(
    sample_mean: float, sample_size: int, pop_mean: float, pop_std: float
) -> float:
    """Consumes a sample mean and size alongside population mean and stdevation
    and produces a sample Z score"""
    return (sample_mean - pop_mean) / (pop_std / sqrt(sample_size))


def calc_and_print_cdf_between(
    variable_unit: str,
    pop_mean: float,
    pop_std: float,
    left_bound: float,
    right_bound: float,
) -> None:
    """Calculates and prints CDF between two bounds"""
    left_cdf = calc_cdf(left_bound, pop_mean, pop_std)
    right_cdf = calc_cdf(right_bound, pop_mean, pop_std)

    cdf_between = right_cdf - left_cdf
    print(
        f"Probability of {variable_unit} between {left_bound} and {right_bound} is {cdf_between}"
    )


def calc_cdf(random_variable: float, pop_mean: float, pop_stddev: float) -> float:
    """Calculates cdf of given random variable against population mean and stdev"""

    return scipy.stats.norm.cdf(calc_z_score(random_variable, pop_mean, pop_stddev))


def calc_and_print_cdf(
    variable_unit: str, random_variable: float, pop_mean: float, pop_stddev: float
) -> None:
    """Calculates CDF and prints to std out"""
    cdf = calc_cdf(random_variable, pop_mean, pop_stddev)
    print(f"Probability of {variable_unit} less than {random_variable} {cdf}")


def calc_and_print_cdf_right(
    variable_unit: str, random_variable: float, pop_mean: float, pop_stddev: float
) -> None:
    """Calculates right tail CDF and prints to std out"""
    cdf = calc_cdf(random_variable, pop_mean, pop_stddev)
    cdf_right_tail = 1 - cdf
    print(
        f"Probability of {variable_unit} greater than {random_variable} {cdf_right_tail}"
    )


def calc_z_score(random_variable: float, pop_mean: float, pop_stddev: float) -> float:
    """Consumes a random variable and the population mean/stddev
    and produces a z score"""
    return (random_variable - pop_mean) / pop_stddev


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--plot")
    args = parser.parse_args()
    should_plot = True
    if args.plot is None:
        should_plot = False
    main(should_plot)
