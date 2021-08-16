import 'package:shared_preferences/shared_preferences.dart';

class Constants {
  void storeLoggedInStatus(bool isLoggedInStatus) async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    prefs.setBool("isLoggedIn", isLoggedInStatus);
  }

  Future<bool> getLoggedInStatus() async {
    SharedPreferences prefs = await SharedPreferences.getInstance();
    return prefs.getBool("isLoggedIn") ?? false;
  }
}
