# stanford-cs-cda
> Stanford CS Courses Data analytics

## Crawling

- goto [this site](https://explorecourses.stanford.edu/print?q=CS+&descriptions=on&academicYear=&catalog=&page=0&filter-coursestatus-Active=on&collapse=&catalog=)
- run this javascript on the console
  ```js
  console.log(
      Array.prototype
           .slice
           .call(document.getElementsByClassName('courseNumber'))
           .map(i => i.innerText.slice(0, i.innerText.length-1).replaceAll(' ',''))
           .join('\n')
  )
  ```
- the result:
  ```
  CS 1C
  CS 1U
  CS 7
  ...
  CS 581
  ```
- **Google Trends** just accepts for only 5 items to compare trend results and to make results more objectively, I choose only US area.
- the template *url* is `https://trends.google.com/trends/explore?date=all&geo=US&q=<item1>,<item2>,<item3>,<item4>,<item5>`
- I arrange *5 courses* per one search:
  ```
  https://trends.google.com/trends/explore?date=all&geo=US&q=CS1C,CS1U,CS7,CS9,CS11SI
  https://trends.google.com/trends/explore?date=all&geo=US&q=CS12SI,CS13SI,CS21SI,CS22A,CS24
  https://trends.google.com/trends/explore?date=all&geo=US&q=CS25,CS28,CS31N,CS41,CS43
  ...
  ```
- Download each report
- Using `process.py` for processing data.

## Result
> *Thứ hai, 31 Tháng 1 năm 2022 01:17:24 +07*

***Top 3***: ['CS50: (United States)', 'CS300: (United States)', 'CS106A: (United States)']

