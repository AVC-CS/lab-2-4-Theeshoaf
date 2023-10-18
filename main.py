def main():

    original_str = 'Python Programming'
    secondP= original_str.find('P',1)
    sub1 = original_str[secondP:]
    sub2 = original_str[:secondP-1]
    
    # sub1 = original_str [7:]
    # sub2 = original_str [:6]
   
    print(sub2)
    print(sub1)
    merged_str = sub1 + ' ' + sub2 
    print(merged_str)

    
    
    return sub1, sub2, merged_str


if __name__ == '__main__':
    main()
