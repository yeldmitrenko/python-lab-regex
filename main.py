import re


def main():
    input_file = "C:\\Users\\user\\PycharmProjects\\lab_5\\log_file.txt"

    regex_1 = r'[1-8]\d\.\d{1,3}\.\d{1,3}\.\d{2,3} - - \[(\d{2}\/\D{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) ' \
              r'\+(0100|2000)] "GET .*?" 200 (.+)'

    regex_2 = r'\[1-8]\d\.\d{1,3}\.\d{1,3}\.\d{2,3} - - \[(\d{2}\/\D{3}\/\d{4}):(\d{2}:\d{2}:\d{2}) ' \
              r'\+(0100|2000)] "POST .*?" 200 (.+)'

    with open(input_file, 'r') as file:
        successful_call_counter_get, successful_call_counter_post = 0, 0
        for line in file.readlines():
            data_1 = re.match(regex_1, line)
            data_2 = re.match(regex_2, line)
            if data_1:
                print(data_1)
                successful_call_counter_get += 1
            elif data_2:
                print(data_2)
                successful_call_counter_post += 1
        print(f'The number of successful GET: {successful_call_counter_get}')
        print(f'The number of successful POST: {successful_call_counter_post}')


if __name__ == '__main__':
    main()
