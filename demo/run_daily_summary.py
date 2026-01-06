from sleeping_gpu_inference.reports.daily_summary import (
    generate_daily_summary,
    print_daily_summary
)

def main():
    summary = generate_daily_summary()
    print_daily_summary(summary)

if __name__ == "__main__":
    main()
