# RegManager

### Overview
Available for Windows OS only.

### Requirements
None

### How to use
1. Import the RegManager
   * ``from RegManager import RegManager``
2. Call the constructor to assign it to a variable
   * ``rm = RegManager('HKEY_CURRENT_USER', 'Software\\ENMSoft', 'Test')``
      * hive is specified as HKEY_CURRENT_USER if not specified
   *  The constructor has the following parameters
      * ``__init__(self, hive: str, key_path: str, value_name: str)``
3. Call the handler, passing in the action you want to use and any additional arguments
   * <span style="color:red">Warning: If the key does not exist in the path specified in the constructor at the moment
   the handler is called, it will be created.</span>
   * ``read_data = rm.handler('read')``
   * ``rm.handler('save', 'hello-world')``
   * Available actions include
      * read
      * save
   * The function prototype looks like this
      * ``handler(self, action: str, save_data: str = None) -> str or None``
4. The return value can be either str or None, depending on the action you passed in
   * read
     * Returns the value of the value, if it exists
     * However, if value is an empty str, None is returned
   * save
     * None is always returned