Writing and running tests

1. Writing tests
    - django.test.TestCase, là  subclass của unittest.TestCase
      nó sẽ chạy mỗi một test trong một transaction để độc lập dữ liệu test.

2. Running tests
    - test all project
    ./manage.py test
    - test only modules or packages

3. The test database
    - Database sử dụng cho test k phải là production database, django tự tạo một empty database
      để thực thi test
    - Khi thực thi test xong ( thành công hoặc thất bại) thì test database luôn được xóa.
    - Để giữ database khi chạy test thì dùng lệnh sau:
         test --keepdb
         Note: Nếu test database k tồn tại thì sẽ tạo mới
    - Một số trường hợp có thể test database không bị xóa, khi chạy lại thì nó sẽ hỏi có xóa database cũ không
      trong trường hợp này có thể dùng câu lệnh
        test --noinput
        Note: Option này sẽ tự động xóa database cũ
    - test Database sẽ tự động tạo với tên test_databasename với databasename setting trong file config.
      Nếu muốn thay đổi test database thì mình thêm một giá trị  có key = 'TEST', và value = configdb.. vào trong
      DATABASES['default'] dictionary
    - If your code attempts to access the database when its modules are compiled, this will occur before the test database is set up,
       with potentially unexpected results. For example, if you have a database query in module-level code and a real database exists,
       production data could pollute your tests. It is a bad idea to have such import-time database queries in your code anyway
       rewrite your code so that it doesn’t do this. This also applies to customized implementations of ready().

3. Order in which tests are executed
    - Chạy kiểu nhiều thread và k quan trọng lắm
    - Có thể đảo ngược thứ tự dựa vào option: test --reverser
